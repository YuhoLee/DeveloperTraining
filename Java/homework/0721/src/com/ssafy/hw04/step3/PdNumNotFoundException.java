package com.ssafy.hw04.step3;

public class PdNumNotFoundException extends Exception{
	private static final long serialVersionUID = 1L;
	
	public PdNumNotFoundException(String pdnum) {
		super("해당 제품이 존재하지 않습니다.");
		System.err.println("<명령 취소>  " + pdnum + " 제품이 존재하지 않습니다.");
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
