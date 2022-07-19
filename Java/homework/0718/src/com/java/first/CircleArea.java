package com.java.first;

public class CircleArea {
	private final double rad = 5;

	public static void main(String[] args) {
		CircleArea c = new CircleArea();
		c.display();
	}

	private void display() {
		System.out.printf("반지름이 " + rad + "인 원의 넓이는 " + String.format("%.1f",rad*rad*Math.PI) + "Cm2입니다.");
	}
}
