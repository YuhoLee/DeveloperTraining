package com.java.second;

public class TV extends Product{
	private int inch;
	private String dpType;
	
	public TV() {
		
	}
	
	public TV(String pdnum, String pdname, int price, int quantity, int inch, String dpType) {
		super(pdnum, pdname, price, quantity);
		this.inch = inch;
		this.dpType = dpType;
	}

	public int getInch() {
		return inch;
	}

	public void setInch(int inch) {
		this.inch = inch;
	}

	public String getDpType() {
		return dpType;
	}

	public void setDpType(String dpType) {
		this.dpType = dpType;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + "\t | " + inch + "\t | " + dpType;
	}
}
