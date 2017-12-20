# Description:

This project serves two goals:
	* Provide a simple method to recreate this configuration on any new computer I use frequently.
	* Share my dotfiles online.

# Screenshots:

![unix_basic](/screenshots/unix_basic.png)
![unix_cava](/screenshots/unix_cava.png)
![unix_cavafull](/screenshots/unix_cavafull.png)
![unix_neofetch](/screenshots/unix_neofetch.png)
![unix_vim](/screenshots/unix_vim.png)

# Installation:

	## Dependencies:
		I have used the following applications:
			conky , cmus , python3 , git
		Additionally ,
			pywal is also used for generating colorschemes but I have not included it in the repository. 
			It's use is trivial - Namely, generate a colorscheme from wallpaper.png, apply it to terminals,
			add one line to .bashrc and add one line to session-startup.

		Installing all dependencies is easy. They are commonly used packages and are in Ubuntu's repository as well.

	## Procedure:
		Once, you installed the dependencies.
		1) Go to your home directory by:
			'cd ~'
		2) Clone this repository by:
			'git clone https://github.com/abhishekkumar2718/conky_conf.git'
		3) Check if there is a folder called ".conky" in your home directory. If there is , delete it.
		4) Run setup.sh as
			'source ~/conky_conf/setup.sh'
		5) If the month is not December of 2017, run gen_cal.py as well:
			'python3 ~/.conky/gen_cal.py'

		### Optional:
		A) wal:
			1) Run wal as 
				'wal -i -t ~/.conky/wallpaper.png'
			2) To apply colorscheme to any new terminal you open, add the following line to your terminal resource file:
				'(wal -r -t &)'
			3) To make colorscheme persist over boots, add the following command to your startup file:
				'wal -R'

		B) cmus:
			If you use any music player other than cmus, edit music_info.sh as per your requirement.

		C) Network Interface:
			Change network interface names "enp4s8", "enp0s29f7u5" in info.rc as per your requirement.
