package com.java.second;
import java.util.Arrays;

public class ProductMgr {
	private Product[] products;
	private int max = 0;
	private int size = 0;
	
	public ProductMgr() {
		products = new Product[max];
	}
	
	public void add(Product pd) {	// 상품정보 추가
		int idx = indexOf(pd.getPdnum());
        if(idx != -1) {
            System.out.println(pd.getPdnum() + " / " + pd.getPdname() + "<----" + "중복되는 상품번호 삽입 시도!! \n<명령 취소>\n");
            return;
        }
		if(size >= max) {
			max += 1;
			products = Arrays.copyOf(products, max);
		}
		products[size++] = pd;
	}
	
	public void remove(String pdNum) {
		if(size <= 0) {			// 등록된 상품이 아무것도 없을 때
			System.out.println("현재 등록된 상품이 없습니다!!! \n<명령 취소>\n"); 
			return;
		}
		
        int index = indexOf(pdNum);
        if(index == -1) {
        	System.out.println("등록되지 않은 상품입니다!!! \n<명령 취소>\n");	// 입력한 번호의 상품이 없을 때
        }
        
        products[index] = products[--size];
    	return;
        
    }
	
	public Product[] getList() {		// 상품정보 전체를 검색
		return products;
	}
	
	public Product searchByNum(String num) {	// 상품번호로 상품 검색
		int idx = indexOf(num);
		if(idx != -1) {
			return products[idx];
		}
		return null;
	}
	
	public Product[] searchByName(String name) {	// 상품이름으로 상품 검색(부분검색 가능)
		int buffMax = 0;
		Product[] buffProducts = new Product[buffMax];
		int buffSize = 0;
		for(int i = 0; i < size; i++) {
			if(products[i].getPdname().contains(name)) {
				if(buffSize >= buffMax) {
					buffMax += 1;
					buffProducts = Arrays.copyOf(buffProducts, buffMax);
				}
				buffProducts[buffSize++] = products[i];
			}
		}
		if(size != 0) { return buffProducts; }
		else { return null; }
	}
	
	public Product[] getTV() {		// TV만 검색
		int buffMax = 0;
		Product[] buffProducts = new Product[buffMax];
		int buffSize = 0;
		for(int i = 0; i < size; i++) {
			if(products[i] instanceof TV) {
				if(buffSize >= buffMax) {
					buffMax += 1;
					buffProducts = Arrays.copyOf(buffProducts, buffMax);
				}
				buffProducts[buffSize++] = products[i];
			}
		}
		if(size != 0) { return buffProducts; }
		else { return null; }
	}
	
	public Product[] getRefrigerator() {		// 냉장고만 검색
		int buffMax = 0;
		Product[] buffProducts = new Product[buffMax];
		int buffSize = 0;
		for(int i = 0; i < size; i++) {
			if(products[i] instanceof Refrigerator) {
				if(buffSize >= buffMax) {
					buffMax += 1;
					buffProducts = Arrays.copyOf(buffProducts, buffMax);
				}
				buffProducts[buffSize++] = products[i];
			}
		}
		if(size != 0) { return buffProducts; }
		else { return null; }
	}
	
	public int getTotalPrice() {
		int sum = 0;
		for(int i = 0; i < size; i++) {
			sum += products[i].getPrice() * products[i].getQuantity();
		}
		return sum;
	}
	
	
	private int indexOf(String pdnum) {
		for(int i = 0; i < size; i++) {
			if(pdnum.equals(products[i].getPdnum())){
				return i;
			}
		}
		return -1;
	}
}
