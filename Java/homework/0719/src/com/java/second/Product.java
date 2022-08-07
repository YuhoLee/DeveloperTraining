package com.java.second;

public class Product {
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
	

	@Override
	public String toString() {
		return pdnum + "\t | " + pdname + "\t\t | " + price + "\t | " + quantity;
	}
}