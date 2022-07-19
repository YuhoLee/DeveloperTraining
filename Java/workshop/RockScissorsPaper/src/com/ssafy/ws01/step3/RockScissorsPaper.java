package com.ssafy.ws01.step3;

import java.util.Scanner;

public class RockScissorsPaper {
	private Scanner sc =  new Scanner(System.in);
	private final int rock = 1;
	private final int scis = 2;
	private final int paper = 3;
	private int rept;
	private int win;
	private int myRsp;
	private int comRsp;
	private int cnt = 0;
	private int myWin = 0;
	private int comWin = 0;
	
	public static void main(String[] args) {
		RockScissorsPaper rsp = new RockScissorsPaper();
		rsp.play();
	}
	
	private void play() {
		this.display();
		while(this.cnt < this.rept) {
			this.enter();
			if(this.calc()) { this.cnt += 1;}
			System.out.println("플레이어: " + this.myWin + ", 컴퓨터: " + this.comWin + ", 판수: " + this.cnt + "\n");
			if(this.judge()) { return;}
		}
	}
	
	private void display() {
		int mode;
		System.out.println("가위바위보 게임을 시작합니다. 아래 보기 중 하나를 고르세요.");
		System.out.println("1. 5판 3승");
		System.out.println("2. 3판 2승");
		System.out.println("3. 1판 1승");
		System.out.print("번호를 입력하세요. ");
		mode = this.sc.nextInt();
		System.out.println("");
		if(mode == 1) {this.rept = 5;}
		else if (mode == 2) {this.rept = 3;}
		else if (mode == 3) {this.rept = 1;}
		this.win = this.rept / 2 + 1;
	}
	
	private void enter() {
			String strRsp;
			System.out.print("가위바위보 중 하나 입력:");
			strRsp = this.sc.next();
			if(strRsp.equals("바위")) {this.myRsp = 1;}
			else if(strRsp.equals("가위")) {this.myRsp = 2;}
			else if(strRsp.equals("보")) {this.myRsp = 3;}
			this.comRsp = (int)(Math.random() * 3) + 1;
	}
	
	private boolean calc() {
		if(this.myRsp == this.comRsp) {
			System.out.println("비겼습니다~~~");
		}
		else if((this.myRsp==this.rock && this.comRsp==this.scis)||(this.myRsp==this.scis && this.comRsp==this.paper)||(this.myRsp==this.paper && this.comRsp==this.rock)) {
			System.out.println("이겼습니다!!!");
			this.myWin += 1;
		}
		else if((this.myRsp==this.scis && this.comRsp==this.rock)||(this.myRsp==this.paper && this.comRsp==this.scis)||(this.myRsp==this.rock && this.comRsp==this.paper)) {
			System.out.println("졌습니다...");
			this.comWin += 1;
		}
		return true;
	}
	
	private boolean judge() {
		if(this.myWin == this.win) {
			System.out.println("### 플레이어 승!!!");
			return true;
		}
		if(this.comWin == this.win) {
			System.out.println("### 컴퓨터 승...");
			return true;
		}
		if(this.cnt == this.rept && this.myWin == this.comWin) {
			System.out.println("### 비겼어요~~~");
			return true;
		}
		return false;
	}
}
