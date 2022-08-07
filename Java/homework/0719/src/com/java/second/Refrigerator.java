package com.java.second;

public class Refrigerator extends Product{
	private int volume;
	
	public Refrigerator() {
		
	}
	
	public Refrigerator(String pdnum, String pdname, int price, int quantity, int volume) {
		super(pdnum, pdname, price, quantity);
		this.volume = volume;
	}

	public int getVolume() {
		return volume;
	}

	public void setVolume(int volume) {
		this.volume = volume;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + "\t | " + volume;
	}
	
}