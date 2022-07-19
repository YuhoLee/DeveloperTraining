package com.java.first;
import java.util.Scanner;

public class CheckPoint {
	private Scanner sc = new Scanner(System.in);
	private int height;
	private int weight;
	private int bmi;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CheckPoint cp = new CheckPoint();
		cp.input();
		cp.calcBMI();
	}
	
	private void input() {
		String[] str = sc.nextLine().split(" ");
		this.height = Integer.parseInt(str[0]);
		this.weight = Integer.parseInt(str[1]);
	}
	
	private void calcBMI() {
		this.bmi = this.weight + 100 - this.height;
		System.out.println("비만수치는 " + this.bmi + "입니다.");
		if(bmi > 0) { System.out.println("당신은 비만이군요"); }
	}

}
