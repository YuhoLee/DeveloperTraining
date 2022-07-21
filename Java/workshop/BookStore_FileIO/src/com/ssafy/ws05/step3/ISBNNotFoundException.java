package com.ssafy.ws05.step3;

public class ISBNNotFoundException extends Exception{
    private static final long serialVersionUID = 1L;
    
    public ISBNNotFoundException(String isbn) {
    	super("해당 제품이 존재하지 않습니다.");
		System.err.println("<명령 취소>  " + isbn + " 제품이 존재하지 않습니다.");
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}
