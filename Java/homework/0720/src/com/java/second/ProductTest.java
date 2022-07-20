package com.java.second;

public class ProductTest {

	public static void main(String[] args) {
		ProductMgrImpl mgr = ProductMgrImpl.getInstance();
		
        mgr.add(new TV("00001", "삼성 대형 고급형 TV", 2339000, 20, 85, "UHD"));
        mgr.add(new TV("00002", "엘지 스탠바이미 TV", 915690, 46, 27, "FHD"));
        mgr.add(new Refrigerator("00003", "삼성 비스포크 냉장고", 1859000, 84, 875));
        mgr.add(new TV("00004", "삼성 KQ 스크린용 TV", 2891190, 51, 85, "UHD"));
        mgr.add(new Refrigerator("00005", "엘지 디오스 고급 냉장고", 2299950, 13, 870));
        mgr.add(new Refrigerator("00006", "캐리어 클라윈드 보급형", 249000, 210, 182));
        
        // 중복되는 상품 삽입
        mgr.add(new Refrigerator("00006", "캐리어 클라윈드 보급형", 249000, 210, 182));
        
        // 제품 전체 목록
        System.out.println("\n********************제품 전체 목록********************");
        for(Product b : mgr.getList()) {
            System.out.println(b);
        }
        
        // TV 전체 목록
        System.out.println("\n********************TV 전체 목록********************");
        for(Product b : mgr.getTV()) {
            System.out.println(b);
        }
        
        // 냉장고 전체 목록
        System.out.println("\n********************냉장고 전체 목록********************");
        for(Product b : mgr.getRefrigerator()) {
            System.out.println(b);
        }
        
        // "삼성" 단어 포함 제품 목록
        String s = "삼성";
        System.out.println("\n********************제품 제목 포함 검색: " + s + "********************");
        for(Product b : mgr.searchByName(s)) {
            System.out.println(b);
        }
        
        // 제품 번호로 상품 검색
        System.out.println("\n********************상품 검색********************\n" + mgr.searchByNum("00002"));
        
        
        int volume = 400;
        int inch = 50;
        
        // 위의 volume 이상의 냉장고 목록 
        System.out.println("\n*****************" + volume + "L 이상의 냉장고 목록" + "*****************");
        for(Product b : mgr.searchVolumeOver(volume)) {
            System.out.println(b);
        }
        
        // 위의 inch 이상의 TV 목록
        System.out.println("\n*****************" + inch + "인치 이상의 TV 목록" + "*****************");
        for(Product b : mgr.searchInchOver(inch)) {
            System.out.println(b);
        }
        
        // "00004"제품번호를 가진 제품 삭제
        mgr.remove("00004");	
        
        // "00005"제품번호를 가진 제품 10개 사기
        // "00008"제품번호를 가진 제품 3개 사기  ---> PdNumNotFoundException 예외 발생
        try {
        	mgr.buy("00005", 10);
        	mgr.buy("00008", 3);
        }catch(PdNumNotFoundException e1) { 	
        }
        
        // "00003"제품번호를 가진 제품 8개 팔기
        // "00001"제품번호를 가진 제품 50개 팔기 ---> QuantityException 예외 발생
        try {
        	mgr.sell("00003", 8);
        	mgr.sell("00001", 50);
        }catch(PdNumNotFoundException e1) {	

        }catch(QuantityException e2) {  

        }
        
        // "00003" 제품번호를 가진 제품 가격 변경 (20% 세일)
        mgr.modifyPrice("00003", (int)(1859000 * 0.8));
        
        // 제품 전체 목록
        System.out.println("\n********************제품 전체 목록********************");
        for(Product b : mgr.getList()) {
            System.out.println(b);
        }
        
        System.out.println("\n제품 가격 총합 : " + mgr.getTotalPrice());


	}

}
