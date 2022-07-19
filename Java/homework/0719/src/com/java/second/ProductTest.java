package com.java.second;

public class ProductTest {

	public static void main(String[] args) {
		ProductMgr mgr = new ProductMgr();
        mgr.add(new TV("00001", "삼성 대형 고급형 TV", 2339000, 20, 85, "UHD"));
        mgr.add(new TV("00002", "엘지 스탠바이미 TV", 915690, 46, 27, "FHD"));
        mgr.add(new Refrigerator("00003", "삼성 비스포크 냉장고", 1859000, 84, 875));
        mgr.add(new TV("00004", "삼성 KQ 스크린용 TV", 2891190, 51, 85, "UHD"));
        mgr.add(new Refrigerator("00005", "엘지 디오스 고급 냉장고", 2299950, 13, 870));
        mgr.add(new Refrigerator("00006", "캐리어 클라윈드 보급형", 249000, 210, 182));
        
        
        System.out.println("\n********************제품 전체 목록********************");
        for(Product b : mgr.getList()) {
            System.out.println(b);
        }
        
        System.out.println("\n********************TV 전체 목록********************");
        for(Product b : mgr.getTV()) {
            System.out.println(b);
        }
        
        System.out.println("\n********************냉장고 전체 목록********************");
        for(Product b : mgr.getRefrigerator()) {
            System.out.println(b);
        }
        
        String s = "삼성";
        System.out.println("\n********************제품 제목 포함 검색: " + s + "********************");
        for(Product b : mgr.searchByName(s)) {
            System.out.println(b);
        }
        
        System.out.println("\n********************상품 검색********************\n" + mgr.searchByNum("00002"));
        
        mgr.remove("00004");	// 삭제
        System.out.println("\n********************제품 전체 목록********************");
        for(Product b : mgr.getList()) {
            System.out.println(b);
        }
        
        System.out.println("\n제품 가격 총합 : " + mgr.getTotalPrice());


	}

}
