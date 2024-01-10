-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 10, 2024 at 06:27 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aopsimol_credential`
--

-- --------------------------------------------------------

--
-- Table structure for table `credential_table`
--

DROP TABLE IF EXISTS `credential_table`;
CREATE TABLE IF NOT EXISTS `credential_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` timestamp NULL DEFAULT NULL,
  `credential` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `credential` (`credential`)
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `credential_table`
--

INSERT INTO `credential_table` (`id`, `datetime`, `credential`, `is_active`) VALUES
(1, '2024-01-10 18:26:13', 'Q6*XU3--RWz:cDcZ!u&JwjqS5EbDSBceC6W,kAmdZ:7{j>(E}#', 1),
(2, '2024-01-10 18:26:13', 's3D~&Ru9Wb[_n<2(!z+:#M/:MU^&S<L+&FEszct[3}jgw-H3cN', 1),
(3, '2024-01-10 18:26:13', 'gWuR[s>bFYpAS]&S6XQ=W_PSEa#7#-=Z:nL~eD/wM{<&wkRD__', 1),
(4, '2024-01-10 18:26:13', 'VYhaRzeXK:jBn^2uqDT;*WhV2t_Ggkb~$!Y;Z[-an[=A86R(8g', 1),
(5, '2024-01-10 18:26:13', 'A[${ZT(PwM?MH]rYkQfzy{9}rK2U^^%^X^CV;x3@x4HS9vuS;V', 1),
(6, '2024-01-10 18:26:13', 'kf}:]>>m:EGg%<(E(S8_a^/AU}KP{=j4#8m&-4m}Y.n+mq>a<r', 1),
(7, '2024-01-10 18:26:13', 'ry,<Ae[+~!X+td4XvB{U+?+(BP>>AF7N_rTW~#aV>;R*e_pCq;', 1),
(8, '2024-01-10 18:26:13', 'wNWk@&7?&/;LZ8WK+&eRW$)A]X)>e<7p$3}<nShLGnA+>7q2ej', 1),
(9, '2024-01-10 18:26:13', 'q;3(K9&[/fVMJzG,{m;;}kgZq/sFDAz-(9>X}]49<vSQb^a,e)', 1),
(10, '2024-01-10 18:26:13', 'jZ;r#[xtta:<H7kCXR5_X+N^[!*+*s2Dmd=!7MEK&9^fR2D2Y=', 1),
(11, '2024-01-10 18:26:13', 'd]?ed[FB<PT_c@T~5vCrVwzcNw[EL2F#EZmCzq!Yr_DWC;)3=w', 1),
(12, '2024-01-10 18:26:13', 'v#T8n2QBM;5+j=n_bF$w:kD$kJgm4VzJFd.2tjq7h@(2_ZY*T5', 1),
(13, '2024-01-10 18:26:13', 'YTgsj:3GFkH+:w;H/]/u>,wDL<?pY/(ah*~,xK)eVF9j*42a+f', 1),
(14, '2024-01-10 18:26:13', 'kr>_tT.;;%<3(3T$z*y<^y?;aH4K5fksU_kac!g=M6^_/LQj7b', 1),
(15, '2024-01-10 18:26:13', 'Nhw&}Bu3sy@(@{{p5z6RrcZ6%z8%h[(;j84-V9cY>!6>7#e^CU', 1),
(16, '2024-01-10 18:26:13', 'c(~L?X{--CGQ/kf*xd/C+_Gs{8p<r~2,B_!k8w3~@&m}L-V]$#', 1),
(17, '2024-01-10 18:26:13', 'gJF9M2zFq$u=QrQCY2<A<p_AE;gp.HYmWafrf&S4YM*?8X;c#C', 1),
(18, '2024-01-10 18:26:13', 'F>;(@pnvP9mtsP*KfD[DUQU-X=y#<Nn2vRvxMHM#54q;DdftbC', 1),
(19, '2024-01-10 18:26:13', 'M=~p;;Y~}Csg^Fq5e8~<5<&~c]b9?Lv&T]m+,2*ek;Q]XrG!zt', 1),
(20, '2024-01-10 18:26:13', 'n64<C$yDbv}));__c~B:7R&et6YMhE$zEXdh]q=82c-9T~$:69', 1),
(21, '2024-01-10 18:26:13', 'y<{f]@r%LB:3YF4khhBgy9;=)N;9!ZY~rHpZf6Y^>Q%dB^eyH/', 1),
(22, '2024-01-10 18:26:13', 'Thgk7,a^<Y^3wNf7yM9]-AuS;A[wT#;=yY9hQ#^z/z>ebKFPJB', 1),
(23, '2024-01-10 18:26:13', 'Zv3TKm]Yba=Vfk37.bEtmu$KWVgA5s&h{U-YpeRkkyQEdd$#c#', 1),
(24, '2024-01-10 18:26:13', 'H7uXs2/nLS%BYbn~r<=:nD-4Th-hHge<8@NB*~eRh;-hjb}?s;', 1),
(25, '2024-01-10 18:26:13', 'N68C$W<A4~A4wGj,79HGAEBP$:eQ%b4[rYURQ!Hbmd^;r&&$L=', 1),
(26, '2024-01-10 18:26:13', 'Qjq8zE2Lh[@w{U]uWs(/<;P6#)*w9nr)q*Z&=6EEf?9U9x(N:u', 1),
(27, '2024-01-10 18:26:13', 'D5;cut3Hv3v7-?eTE&Yu[J38j%,b-Fc$UQqf~#@:($PgL5@&;P', 1),
(28, '2024-01-10 18:26:13', 'aGCsv)[NNY>$xb2+8ya_4mDK:A#;MjC2?NYua;(GkAd,j,MHSG', 1),
(29, '2024-01-10 18:26:13', 'uG4^9SCy@.xn/QM5JDdE~{9K]^kYn2hc.V2Dys7FfRW^)^R}#?', 1),
(30, '2024-01-10 18:26:13', 'cha;c!9Y~z>~r!Q$Lfp6V].cf;u}SAA4HyD{:vW6hMyu3{6XSZ', 1),
(31, '2024-01-10 18:26:13', 'N]Td.g?d(8CB,ff;r9Vs!b5;hv{p35&-94Nt<,UZ!:W7pKh%wk', 1),
(32, '2024-01-10 18:26:13', 'G$=~7&*w;e.?7,-)qzm@}eyL**9Qt;,L4V<824FZE=~$d!m+7U', 1),
(33, '2024-01-10 18:26:13', 'DhC^,tpj!49ct(zE:jqbXV)r@,>f#Rm=YevL8Fa!+{,vM+L$-y', 1),
(34, '2024-01-10 18:26:13', 'JQ[kwf5j;6{.ta(vW*5Eg:!~??JSZuE;#;W4f}M~cQS:ZV-~-U', 1),
(35, '2024-01-10 18:26:13', 'T&UX#m2!eYM)bKH<m&;<#5dPf]j(gHu~2Ug:b[?CU-S;LK7>e&', 1),
(36, '2024-01-10 18:26:13', 'b!kv44N]WY$sJs.&p@3@?7H^nD;H-#Cm=x}7QCrM=4)ns){t;]', 1),
(37, '2024-01-10 18:26:13', 'ngVd}y.CsgH>K2WgXLd?!y@$gvCjw=98;yN{3T55[7}AHM=pXZ', 1),
(38, '2024-01-10 18:26:13', 'W^p&c.}+zQj3{(vXHsu(.=yL6BYYT&rT[{e*;=*Z=^2*=9xadB', 1),
(39, '2024-01-10 18:26:13', 'EwgGh4yP&&SKW26q.Q=+x-2/$&Y.phpaH,rK$*:ecA$4RN#M)F', 1),
(40, '2024-01-10 18:26:13', 'Lt.fELU2;(kPZbhdF:F{?T_LaFurM4>k?.-{(>8-msRby%H2TS', 1),
(41, '2024-01-10 18:26:13', 'AY&~4x~PDhR]kLCe%{F%3)X9TB.tVRZ7(J3jU_c]j%DRuLNAvR', 1),
(42, '2024-01-10 18:26:13', 'G,}6;^]CP$yMDpbdt6^dFT5gaT<#UHYFMv.&vHr].P>,MVb9=M', 1),
(43, '2024-01-10 18:26:13', 'atz8gK<U.:7S55FF8a^5:HNGKP%BY=9hyG;zzU;_cy$RZ4_Zs?', 1),
(44, '2024-01-10 18:26:13', 'Eg!k-jR#RRX;PACRp@4E59MKe[@d[Fg&mtYBJ8z*BaWSEWc^k^', 1),
(45, '2024-01-10 18:26:13', 'L<Dn;4wuJ-+6VB.H9=(w(?849bq^s>G5D3v3jrt2CR]jB(=;;w', 1),
(46, '2024-01-10 18:26:13', 'FPR/7G%M/CY3dkQF)%Q^3csV3a68W:%-8N<3m~/V;MQ@UE}Wm4', 1),
(47, '2024-01-10 18:26:13', 'dv.R~9Nq@V2X5^9H+S7~Ypa;;jG?zN/e58r=.DXv<RfavFhUeT', 1),
(48, '2024-01-10 18:26:13', 'nwG},++57+Cpe{Z(aG,d_VQs&JnX48GjaYkxwZq*L;As$-#8,C', 1),
(49, '2024-01-10 18:26:13', 'z=Xp~_Vpw(ZbK97b(4dG,*(MqPnaP:,&_65;P[x&+sqfXW#4T*', 1),
(50, '2024-01-10 18:26:13', 'J~Cw]J[}Uu&x9SD%CZ,}vDLj5E>6tkD;,!je;R:t(RsCkQEn3:', 1),
(51, '2024-01-10 18:26:13', 'uEQdKnE7&r,BqP6h7UJ}k(eHvc5g)UB(}--pM^TnW3]PKCrdv[', 1),
(52, '2024-01-10 18:26:13', 'X_~)~^e>jjqJ3c$2sc2rh777&TKUe<h$4XMEG*<ExKv]h-EA@q', 1),
(53, '2024-01-10 18:26:13', 'L8T5k:mS9(HuygGQh;-$Tt<zdV4C/3/KfCV-+.;d&djvJAHf@A', 1),
(54, '2024-01-10 18:26:13', 'RDF{eu8mL}>J>Z^,4q7G@,*gF=Vx/9;Cd/L>E+hMBku7)uz3/C', 1),
(55, '2024-01-10 18:26:13', 'H;*5L5mGN2)}<^69!VBXarS#>P~W)gSdLqDXe6=;]w<N>2Z,mt', 1),
(56, '2024-01-10 18:26:13', 'r+<;%Hwmr:=:8thfbaytL.,EWrBnmxWM-!rZ+2r433Abt>J?(V', 1),
(57, '2024-01-10 18:26:13', 'G6H$k+.q$;Wq=5t(Uaq_#PtCfe~+z7cYH7x{4$J(vq5Fy&vyYH', 1),
(58, '2024-01-10 18:26:13', 'eA-bkNw@.4;(d_*w{J]TJGR4/KHm(]g8zW2K4r~F(.d6*rtVAt', 1),
(59, '2024-01-10 18:26:13', 'C9MC(XdM&v:!wLmY2LNY(]5n7v:f:%R9R^a-h~2vuJ7BFs!hx@', 1),
(60, '2024-01-10 18:26:13', 'N>?!JYCBh>Bp8Vn2;b_}^Bkj*>,?x~}}*X;T;r]7=Rm*9Qw@w_', 1),
(61, '2024-01-10 18:26:13', 'qfq?{)GU2a6!y^W4}-4j7Yues2HB[%V}[){j+X_q6RE,*93/6y', 1),
(62, '2024-01-10 18:26:13', 'vR*DXspM#%!x3PJJ$AKwS>->=A{=a,jsS/:4gnhu*jj;F@&c#V', 1),
(63, '2024-01-10 18:26:13', 'vhR3z)9A$K+{Vr%)!?&Yj*~-p+!~:tQGnQ#M/dwLa36EQnrfn>', 1),
(64, '2024-01-10 18:26:13', 'Y=R;g%<!T;(/f[}rd,,}/yZ43yH&yGu$:]C8@_cR&~mr}nkr{#', 1),
(65, '2024-01-10 18:26:13', 'qw]pnF643jbL$&t_6{XEXvuY5<[k*:^nK#<n_~Vu!:%jpbnkG9', 1),
(66, '2024-01-10 18:26:13', 'qD?ska/$yW:Y+,X@G$XcH8nR27-(jM77Rz7F)daKx6u]-$YmZ{', 1),
(67, '2024-01-10 18:26:13', 'tXppYBnPw9Ya}u3xP!sB$VP%WJ-D^Nx,]jRPDHr@~_}[m;+^7}', 1),
(68, '2024-01-10 18:26:13', 'z-fdz>z9mbg9G9DPDxrPebWA.Cty[N&>LK<B%rgsP@;$tB@9AP', 1),
(69, '2024-01-10 18:26:13', 't(;4+rd]};+>Y(-_kv4xk#5ChV}j6pysFeUZ,@4)@RuT)XXePe', 1),
(70, '2024-01-10 18:26:13', 'S7,x_e^@y+YU.H!nj<g{wL;2Jp?8Cs](p,StWCjbJbPNHY*Cx{', 1),
(71, '2024-01-10 18:26:13', 'tGD@xe,ynZeb>>[BA9eH2+@+7:U=W2<>E#;^DkE&{Eq3Gw5k=x', 1),
(72, '2024-01-10 18:26:13', 'c6q,t;YTrwT:u@?4*Rbm^c)4ymbgx-r3VJ_]3>.G*J%xG%Nyfu', 1),
(73, '2024-01-10 18:26:13', 'W;7.{WM3*nnf$ruy2]]yc.MEXurH4}4!%M9Eg9Dnw/bAC2vP.8', 1),
(74, '2024-01-10 18:26:13', 'zv!gaK5]<pQ,h8M{N$d?kA5}z*;&S9Y^k(CV@xmaB*8t=c<bS-', 1),
(75, '2024-01-10 18:26:13', 'xC/-6S;rTTH*Qd[JC@_f~Rgpc(E!<uJGTQ6h*;m$j#rAv./RPP', 1),
(76, '2024-01-10 18:26:13', 'nHevY8/#5zKkr,2E_79N)@@evuJ;^A+%v;{FzR6GhzX#TWp{Nt', 1),
(77, '2024-01-10 18:26:13', 'X{HtvF[3;{JV2=,]V~!S#4s~d*HU{LB2>*NX=?/F!X8f3gHr3;', 1),
(78, '2024-01-10 18:26:13', 'dW*$TA4T-MkZKe/wLx}Tq7J).=#fs$]wXjK_*Jev>BZ5;pj3fa', 1),
(79, '2024-01-10 18:26:13', 'XxXTp8$H-e-c?;5SqKsMjYbNS~&[tYBP_#N7&bzFHau.rdt:RW', 1),
(80, '2024-01-10 18:26:13', 'G]S_S+}[3zVqSd!]6D*>&;ZJVZ^@Qu+{5G<uaMs}W-.S9CXm3b', 1),
(81, '2024-01-10 18:26:13', 'X$:kdZq@e,.z*Jy8Y@nhx}Lawe$~eW>d4$A{:+qM(ns!ew%,du', 1),
(82, '2024-01-10 18:26:13', 'LX%FRqt8y*:J:=LU&S>n4c?)n>ZW6Db#H&8Y@_3*ps6PU)+a;W', 1),
(83, '2024-01-10 18:26:13', 'kgCck2HC8,6gVNa}TFMjB.a3*ev^}ffSxp,5+/C9[[rL46Ep#:', 1),
(84, '2024-01-10 18:26:13', 'uWEdYdhTk>&ctY@^)sy35:*k/<ctRK8mc/YCK.u=sU&(pKNsy;', 1),
(85, '2024-01-10 18:26:13', 'bujf[}<;KG7a8{u5P>E}+DZDRRrn;(hqpJZ);^$bPj]Qkz7JT@', 1),
(86, '2024-01-10 18:26:13', 'yP&w4jUM_$TxXd}npy]^c[/YT)gqQjRM&Ssr*8u?v*]~VE5NdM', 1),
(87, '2024-01-10 18:26:13', 'K!c~m/gt?VkYN,]7!k/YtqBKh&cV!{[G9;rc=v:Uv-JU6@cfrR', 1),
(88, '2024-01-10 18:26:13', 'mpMwgg3CNs9s;D3zMmyF8_MU>:]s28qk;B{pUhM:Ka;pB5z[${', 1),
(89, '2024-01-10 18:26:13', 'Ydf)3w;Ks(8Ugf7!;CJa,^KU*:)~B5eU*atNGgtq7LvkpUd<!(', 1),
(90, '2024-01-10 18:26:13', 'JHdUPp6j%{(;@][sak/;gy&m{ejY[8!gJ:_zS6X/W(}~&RPYw7', 1),
(91, '2024-01-10 18:26:13', 'ZBN(NB5pNj[{2>Yxg7H*Y>!x4BhQrRw+qz>:MzrAFjD(smF!F~', 1),
(92, '2024-01-10 18:26:13', 'YPUbSS{&&KA<UbvG~q=-S=c6~k%CpG=33&p?6?6/Nn@Ffk[a}E', 1),
(93, '2024-01-10 18:26:13', 'zA%k^Y5,pskB?){eB-FWp$]P$w/Tx>.r<qU!A9eu,9pMT]EYwy', 1),
(94, '2024-01-10 18:26:13', 'tp?Rkr?k;HGQ7M-P(Y8KPz]N(RYN5>d4BB;C[_d{LC=VcyPT3}', 1),
(95, '2024-01-10 18:26:13', 'E,v.^v&=C%~XfKw:jw2QU-v3h?<F;Q3pXFXCa@YPnyRm](2u<Q', 1),
(96, '2024-01-10 18:26:13', 'Zp=4E(G-3Z*!5$}SXCSuy,=c+ZJD(2rd${T7_<4t/a[B),s@bW', 1),
(97, '2024-01-10 18:26:13', 'q7wQ&_2,k>%yuDqXe/)Ng(jz4.)]u:+MPE5hcw&X9tQC*4G7?Y', 1),
(98, '2024-01-10 18:26:13', 'FV59p#!&D-)C<c)KtTTQv<R.Qtx^%:wPbNsud@3U)f8/)#m,e,', 1),
(99, '2024-01-10 18:26:13', 'P[5yYuZRYy?8LFVZ8?Q)bbjTwm-!ES7<DNU)26[7Y:*4LR<S;)', 1),
(100, '2024-01-10 18:26:13', 'bvh$r=)>xH}d9S2aVH_)NMZ4X#DG,9U9Sx,@<vqZx)N4NuJfas', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
