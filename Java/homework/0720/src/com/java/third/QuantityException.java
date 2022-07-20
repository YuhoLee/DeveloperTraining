package com.java.third;

public class QuantityException extends Exception{
	private static final long serialVersionUID = 1L;
	
	public QuantityException(Product pd) {
		super("해당 제품의 수량이 부족합니다.");
		System.err.println("<명령 취소>  " + pd.getPdnum() + " " + pd.getPdname() + " 제품의 수량이 부족합니다.  ( 남은 수량: " + pd.getQuantity() + " )");
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
