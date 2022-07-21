package com.ssafy.hw04.step3;
import java.io.EOFException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Arrays;

public class ProductMgrImpl {
	private static ProductMgrImpl mgr;	
	private ArrayList<Product> products;
	private File target = new File("book.dat");
	
	public static ProductMgrImpl getInstance() {
		if(mgr == null) {
			mgr = new ProductMgrImpl();
		}
		return mgr;
	}
	
	public ProductMgrImpl() {
		products = new ArrayList<>();
		loadData();
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void add(Product pd) {	// 상품정보 추가
		int idx = indexOf(pd.getPdnum());
        if(idx != -1) {
            System.err.println("<명령 취소>  \"" + pd.getPdnum() + "  " + pd.getPdname() + "\"  <----  " + "중복되는 상품번호 삽입 시도!!");
            try {
				Thread.sleep(200);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
            return;
        }
        else {
        	products.add(pd);
        }
	}
	
	public void remove(String pdNum) {
		if(products.size() <= 0) {			// 등록된 상품이 아무것도 없을 때
			System.out.println("\n<명령 취소>현재 등록된 상품이 없습니다!!! \n"); 
			return;
		}

        int index = indexOf(pdNum);
        if(index == -1) {
        	System.err.println("\n<명령 취소>  등록되지 않은 상품입니다!!! \n");	// 입력한 번호의 상품이 없을 때
        	return;
        }        
        products.remove(index);
    }
	
	public ArrayList<Product> getList() {		// 상품정보 전체를 검색
		return products;
	}
	
	public Product searchByNum(String num) {	// 상품번호로 상품 검색
		int index = indexOf(num);
		if(index != -1) {
			return products.get(index);
		}
		return null;
	}
	
	public ArrayList<Product> searchByName(String name) {	// 상품이름으로 상품 검색(부분검색 가능)
		ArrayList<Product> nameProducts = new ArrayList<>();
		for(Product p: products) {
			if(p.getPdname().contains(name)) {
				nameProducts.add(p);
			}
		}
		if(!nameProducts.isEmpty()) {
			return nameProducts;
		}
		else { return null; }
	}
	
	public ArrayList<TV> getTV() {		// TV만 검색
		ArrayList<TV> tvs = new ArrayList<>();
		for(Product p: products) {
			if(p instanceof TV) {
				tvs.add((TV)p);
			}
		}
		if(!tvs.isEmpty()) {
			return tvs;
		}
		else { return null; }
	}
	
	public ArrayList<Refrigerator> getRefrigerator() {		// 냉장고만 검색
		ArrayList<Refrigerator> refri = new ArrayList<>();
		for(Product p: products) {
			if(p instanceof Refrigerator) {
				refri.add((Refrigerator)p);
			}
		}
		if(!refri.isEmpty()) {
			return refri;
		}
		else { return null; }
	}
	
	public ArrayList<Refrigerator> searchVolumeOver(int volume){
		ArrayList<Refrigerator> refri = getRefrigerator();
		for(int i = 0; i < refri.size(); i++) {
			if(refri.get(i).getVolume() < volume) {
				refri.remove(i);
			}
		}
		return refri;
	}
	
	public ArrayList<TV> searchInchOver(int inch){
		ArrayList<TV> tv = getTV();
		for(int i = 0; i < tv.size(); i++) {
			if(tv.get(i).getInch() < inch) {
				tv.remove(i);
			}
		}
		return tv;
	}
	
	public void modifyPrice(String pdnum, int price) {
		Product pd = searchByNum(pdnum);
		System.out.println("\n( 가격변경 )  \"" + pd.getPdnum() + " " + pd.getPdname() + "\"  :  " + pd.getPrice() + " ---> " + price);
		pd.setPrice(price);
		
	}
	
	public int getTotalPrice() {
		int total = 0;
        for(Product b: products) {
            total += b.getPrice() * b.getQuantity();
        }
        return total;
	}
	
	 public void sell(String pdnum, int quantity) throws PdNumNotFoundException, QuantityException{
	        Product pd = searchByNum(pdnum);
	        if(pd == null) {
	            throw new PdNumNotFoundException(pdnum);
	        }
	        else {
	            if(pd.getQuantity() < quantity) {
	                throw new QuantityException(pd);
	            }
	            else {
	                pd.changeQuantity(-1 * quantity);
	                System.out.println("\n( Sell )  \"" + pd.getPdnum() + " " + pd.getPdname() + "\" 제품을 " + quantity + "개 팔았습니다.");
	            }
	        }
	    }
		
	public void buy(String pdnum, int quantity) throws PdNumNotFoundException {
        Product pd = searchByNum(pdnum);
        if(pd == null) {
            throw new PdNumNotFoundException(pdnum);
        }
        else {
            pd.changeQuantity(quantity);
            System.out.println("\n( Buy  )  \"" + pd.getPdnum() + " " + pd.getPdname() + "\" 제품을 " + quantity + "개 샀습니다.");
        }
    }
	
	
	private void loadData() {
		new Thread(()->{
			try {
				System.out.println("-------------------- 데이터 로드 --------------------\n");
				ObjectInputStream ois = new ObjectInputStream(new FileInputStream(target));
				products = (ArrayList) ois.readObject();
			} catch(ClassNotFoundException e) {
				e.printStackTrace();
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				System.err.println("파일을 찾을 수 없습니다. 파일을 새로 생성합니다.\n");
				try {
					target.createNewFile();
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			} catch (IOException e) {
				System.err.println("불러올 내용이 없습니다.\n");
			}
		}).start();
	}
	
	public void saveData() {
		try {
			ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(target));
			oos.writeObject(products);
			System.out.println("\n-------------------- 데이터 저장 --------------------\n");
			oos.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	
	private int indexOf(String pdnum) {
		int i = 0;
        for(Product p: products) {
            if(pdnum.equals(p.getPdnum())) {
                return i;  
            }
            i += 1;
        }
        return -1;      // 동일한 idex 없음
	}
}
