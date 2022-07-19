package com.ssafy.ws05.step3;

public class BookTest {
    
    public static void main(String[] args) {
        BookManager bm = new BookManager();
        bm.add(new Book("00001", "자바를 자바라", "홍길동", "SSAFY", 11000, "교재"));
        bm.add(new Book("00002", "앵무새 죽이기", "이사장", "외국기업", 12000, "소설"));
        bm.add(new Magazine("00003", "내셔널지오그래픽", "이자연", "북극곰출판사", 10000, "잡지", 2022, 07));
        bm.add(new Book("00004", "자바를 부셔라", "누굴까", "SSAFY", 16000, "교재"));
        bm.add(new Book("00005", "나는야 자바돌이", "자바맨", "SSAFY", 13000, "교재"));
        bm.add(new Magazine("00006", "디스커버리", "김자연", "미어캣출판사", 10000, "잡지", 2022, 03));
        bm.add(new Magazine("00006", "내셔널지오그래픽", "이자연", "북극곰출판사", 10000, "잡지", 2022, 07));  // 똑같은 도서번호 삽입
        
        System.out.println("\n********************도서 전체 목록********************");
        for(Book b : bm.getList()) {
            System.out.println(b);
        }
        
        System.out.println("\n********************일반 전체 목록********************");
        for(Book b : bm.getBooks()) {
            System.out.println(b);
        }
        
        System.out.println("\n********************잡지 전체 목록********************");
        for(Book b : bm.getMagazine()) {
            System.out.println(b);
        }
        
        String s = "자바";
        System.out.println("\n********************도서 제목 포함 검색: " + s + "********************");
        for(Book b : bm.searchByTitle(s)) {
            System.out.println(b);
        }
        
        System.out.println("\n도서 가격 총합 : " + bm.getTotalPrice());
        System.out.println("도서 가격 평균 : " + bm.getPriceAvg());
        
    }

}
;