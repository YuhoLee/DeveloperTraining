package com.ssafy.hw04.step3;

import java.io.Serializable;

public class Product implements Serializable{
	private String pdnum;
	private String pdname;
	private int price;
	private int quantity;
	
	public Product() {
		
	}
	
	public Product(String pdnum, String pdname, int price, int quantity) {
		this.pdnum = pdnum;
		this.pdname = pdname;
		this.price = price;
		this.quantity = quantity;
	}
	
	public String getPdnum() {
		return pdnum;
	}

	public void setPdnum(String pdnum) {
		this.pdnum = pdnum;
	}

	public String getPdname() {
		return pdname;
	}

	public void setPdname(String pdname) {
		this.pdname = pdname;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public int getQuantity() {
		return quantity;
	}

	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	
	
	public void changeQuantity(int n) {
		 this.quantity += n;
	}

	@Override
	public String toString() {
		return pdnum + "\t | " + pdname + "\t\t | " + price + "\t | " + quantity;
	}
}
