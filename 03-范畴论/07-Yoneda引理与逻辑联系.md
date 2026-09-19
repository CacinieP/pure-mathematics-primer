# Yoneda 引理与逻辑联系：通过所有测试对象认识一个对象

先修：[函子](02-函子与结构保持.md)、[自然变换](03-自然变换.md)、[伴随](06-伴随与自由构造.md)。为使函子范畴的大小明确，本章取 $\mathcal C$ 为小范畴，集合论背景为 ZFC。

## 1. 一个对象如何回答外部问题

在集合中，从单元素集合到 $A$ 的函数相当于选择 $A$ 的一个元素。但在群范畴中，从平凡群到 $G$ 只有一个同态，不能靠它看见 $G$ 的全部结构。

于是把测试对象从一个扩展到所有 $X$：记录全部箭头 $X\to A$，并记录更换测试对象时这些箭头怎样变化。Yoneda 引理说明，这种带相容性的记录拥有很强的识别能力。

“所有测试”指态射集合及其前复合作用，不只是每个集合有多少元素，也不是任意一张对象关系图。

## 2. 固定方差：预层与可表预层

本章使用反变版本。预层是函子

$$
F:\mathcal C^{\mathrm{op}}\to\mathbf{Set}.
$$

对原范畴中的 $u:X'\to X$，它给出 $F(u):F(X)\to F(X')$。

对象 $A$ 对应的可表预层定义为

$$
yA=\mathcal C(-,A),\qquad (yA)(X)=\mathcal C(X,A).
$$

对 $u:X'\to X$，其作用是前复合：

$$
(yA)(u)(f)=f\circ u.
$$

一个预层若自然同构于某个 $yA$，称为可表。并非每个预层都可表。

## 3. Yoneda 引理的准确陈述

存在自然双射

$$
\operatorname{Nat}(yA,F)\cong F(A),
\qquad
\alpha\longmapsto\alpha_A(\operatorname{id}_A).
$$

左边是从可表预层 $yA$ 到 $F$ 的自然变换集合。方向是“从可表预层出发”，不能随意交换为 $\operatorname{Nat}(F,yA)$。

这个式子说：给出一整族与所有测试变化相容的函数 $\alpha_X$，所需信息恰好等于 $F(A)$ 中的一个元素。下面直接写出逆映射，并证明它工作。

## 4. 从一个元素构造全部分量

给定 $a\in F(A)$，对每个对象 $X$ 定义

$$
\alpha^a_X:\mathcal C(X,A)\to F(X),
\qquad
\alpha^a_X(f)=F(f)(a).
$$

类型正确，因为 $f:X\to A$ 使反变函子给出 $F(f):F(A)\to F(X)$。

检查自然性：对 $u:X'\to X$，

$$
\begin{aligned}
F(u)(\alpha^a_X(f))
&=F(u)(F(f)(a))\\
&=F(f\circ u)(a)\\
&=\alpha^a_{X'}(f\circ u).
\end{aligned}
$$

中间一步用了反变复合规律 $F(f\circ u)=F(u)\circ F(f)$。这恰好是 $\alpha^a:yA\Rightarrow F$ 的自然性条件。

再把它放回引理的评价映射：

$$
\alpha^a_A(\operatorname{id}_A)
=F(\operatorname{id}_A)(a)=a.
$$

因此从元素出发再评价，会回到原元素。

## 5. 为什么任意自然变换都由这个元素决定

反过来，给定自然变换 $\alpha:yA\Rightarrow F$，令

$$
a=\alpha_A(\operatorname{id}_A).
$$

对任意 $f:X\to A$，自然性给出交换方形：

$$
\begin{array}{ccc}
\mathcal C(A,A)&\xrightarrow{\alpha_A}&F(A)\\
{\scriptstyle(-)\circ f}\downarrow&&\downarrow{\scriptstyle F(f)}\\
\mathcal C(X,A)&\xrightarrow{\alpha_X}&F(X).
\end{array}
$$

把左上角元素 $\operatorname{id}_A$ 送到右下角，两条路径相等，所以

$$
\alpha_X(f)
=F(f)(\alpha_A(\operatorname{id}_A))
=F(f)(a).
$$

这说明 $\alpha=\alpha^a$。两方向互逆，双射证明完成。证明里真正发挥力量的是对每个 $f$ 的自然性，而不是某种额外的“整体直觉”。

双射对 $F$ 自然：给 $\beta:F\Rightarrow G$，$\beta\circ\alpha$ 对应的元素是 $\beta_A(a)$。它也对 $A$ 自然：给 $u:A\to B$，从 $\operatorname{Nat}(yB,F)$ 预复合 $yu:yA\Rightarrow yB$，对应 $F(u):F(B)\to F(A)$。这也再次核对了反变方向。

## 6. 一个能全部数完的例子

令 $\mathcal C$ 是偏序 $0<1$ 对应的范畴，非恒等箭头记为 $h:0\to1$。定义预层

$$
F(0)=\{a,b\},\qquad F(1)=\{u\},\qquad F(h)(u)=a.
$$

先看 $y0$：

$$
(y0)(0)=\{\operatorname{id}_0\},\qquad (y0)(1)=\varnothing.
$$

自然变换 $y0\Rightarrow F$ 的 0 分量可以把 $\operatorname{id}_0$ 送到 $a$ 或 $b$；1 分量是空集出发的唯一函数。自然性在空域上自动成立，因此共有两个自然变换，对应 $F(0)$ 的两个元素。

再看 $y1$：

$$
(y1)(0)=\{h\},\qquad(y1)(1)=\{\operatorname{id}_1\}.
$$

1 分量只能把 $\operatorname{id}_1$ 送到 $u$。自然性随即迫使 0 分量把 $h$ 送到 $F(h)(u)=a$。所以恰有一个自然变换，对应 $F(1)$ 的唯一元素。

这展示了自然性如何删掉原本看似可以自由选择的分量值。

## 7. Yoneda 嵌入：对象确定到什么程度

在引理中取 $F=yB$，得到

$$
\operatorname{Nat}(yA,yB)\cong\mathcal C(A,B).
$$

具体地，$u:A\to B$ 对应自然变换 $yu$，其分量把 $f:X\to A$ 送到 $u\circ f:X\to B$。

因此

$$
y:\mathcal C\to[\mathcal C^{\mathrm{op}},\mathbf{Set}]
$$

是充满忠实函子，称为 Yoneda 嵌入。尽管每个 $yA$ 是反变预层，对象 $A\mapsto yA$ 组成的嵌入却对 $A$ 协变。

若 $yA$ 与 $yB$ 自然同构，对应的两个相反方向自然变换给出 $u:A\to B$ 和 $v:B\to A$；复合自然变换是恒等，通过上述 Hom 双射得到 $vu=\operatorname{id}_A$、$uv=\operatorname{id}_B$。所以 $A\cong B$。

正确结论是对象由这个完整的 Hom 预层确定到同构。只知道每个 $\mathcal C(X,A)$ 的基数，而丢掉前复合作用与自然性，不能直接调用这个结论。

另有协变版本：对 $H:\mathcal C\to\mathbf{Set}$，

$$
\operatorname{Nat}(\mathcal C(A,-),H)\cong H(A).
$$

这是相反范畴上的相应结果，不应把它的 $\mathcal C(A,-)$ 与本章预层版本的 $F$ 混写。

## 8. 量词也可以成为伴随：先在集合中计算

以下联系来自范畴逻辑；它不是说 Yoneda 引理本身就等于量词理论。

给函数 $f:X\to Y$，把子集看作谓词。逆像

$$
f^*:\mathcal P(Y)\to\mathcal P(X),\qquad f^*(B)=f^{-1}[B]
$$

对应沿 $f$ 代入谓词。另定义

$$
\exists_f(A)=f[A],
\qquad
\forall_f(A)=\{y\in Y:f^{-1}[\{y\}]\subseteq A\}.
$$

直接像与逆像满足

$$
\exists_f(A)\subseteq B
\quad\Longleftrightarrow\quad
A\subseteq f^*(B).
$$

证明只需展开：左边说每个 $a\in A$ 的像在 $B$ 中，正是右边的成员条件。

逆像与全称运算满足

$$
f^*(B)\subseteq A
\quad\Longleftrightarrow\quad
B\subseteq\forall_f(A).
$$

左边说凡是像落在 $B$ 的 $x$ 都在 $A$ 中；按 $y\in B$ 分组，恰好说每个相应纤维全部落在 $A$ 中。

把幂集按包含关系看成偏序范畴，这两组等价就是伴随：

$$
\exists_f\dashv f^*\dashv\forall_f.
$$

不存在性的纤维也必须处理。若 $f^{-1}[\{y\}]=\varnothing$，则 $y$ 总属于 $\forall_f(A)$，因为空集包含于任何 $A$；它不会仅凭空纤维属于 $\exists_f(A)$。

具体取 $X=\{0,1,2\}$、$Y=\{u,v,w\}$，$f(0)=f(1)=u$、$f(2)=v$。对 $A=\{0,2\}$，

$$
\exists_f(A)=\{u,v\},\qquad
\forall_f(A)=\{v,w\}.
$$

$u$ 的纤维包含不在 $A$ 中的 1，所以不满足全称条件；$w$ 的空纤维则满足。

取 $f$ 为投影 $X\times Y\to Y$，把 $A\subseteq X\times Y$ 视为二元谓词，就得到熟悉的“存在 $x$”与“对所有 $x$”对 $x$ 的消去。

## 9. 合取、蕴涵与范畴逻辑的边界

在 $\mathcal P(S)$ 中，交集是积。定义

$$
A\Rightarrow B=(S\setminus A)\cup B,
$$

可以逐元素证明

$$
C\cap A\subseteq B
\quad\Longleftrightarrow\quad
C\subseteq(A\Rightarrow B).
$$

这是“与 $A$ 合取”及“由 $A$ 蕴涵”的伴随关系。幂集给出 Boolean 逻辑；更一般的 Heyting 代数仍有这样的蕴涵伴随，却不必满足所有排中律。

在更一般的范畴中，积与指数对象为简单类型函数和相应直觉主义逻辑片段提供语义；拓扑斯还具有子对象分类器等结构，支持更系统的内部逻辑。这些解释都需要明确的额外结构。不是每个范畴都自动具备量词、函数空间或完整的逻辑体系。

因此，逻辑和范畴论的联系很深，但它们仍是可以独立发展的研究领域。这里的有限集合计算是桥梁的一个可验证入口。

## 10. 练习与解答

**练习 1。** 在第 6 节的范畴中，存在自然变换 $y1\Rightarrow y0$ 吗？

**解答。** 不存在。1 分量需要一个从 $\{\operatorname{id}_1\}$ 到空集的函数，无法定义。这与 $\mathcal C(1,0)=\varnothing$ 完全一致。

**练习 2。** 能否由 Yoneda 写 $\operatorname{Nat}(F,yA)\cong F(A)$？

**解答。** 不能。引理分类的是从可表函子出发的自然变换；任意交换方向一般没有这条结论。连其显式逆映射 $f\mapsto F(f)(a)$ 都不再具有所需类型。

**练习 3。** 仍用第 8 节的 $f$，计算 $\forall_f(\varnothing)$ 和 $\exists_f(\varnothing)$。

**解答。** 分别为 $\{w\}$ 与 $\varnothing$。前者包含全部空纤维的位置，后者没有任何见证。

**练习 4。** 若 $S=\{0,1,2\}$、$A=\{0,1\}$、$B=\{1\}$，求 $A\Rightarrow B$。

**解答。** $(S\setminus A)\cup B=\{1,2\}$。条件 $C\cap A\subseteq B$ 恰好禁止 $0\in C$，因此等价于 $C\subseteq\{1,2\}$。

## 11. 后续路线与参考

继续学习可以沿三条路线展开：用可表函子理解代数几何中的模问题；用极限、伴随与同调方法理解结构；用 Heyting 代数、拓扑斯和类型论理解内部逻辑。本章的引理证明已经完整，但这些方向各自还需要新的对象与定理。

Yoneda 的方差和评价映射可核对 [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf)第 2 章，量词伴随见其第 4 章；也可读 [Basic Category Theory](https://arxiv.org/abs/1612.09375)第 4 章。两份资料均由作者公开提供；本章先用小范畴避开更一般表述中的大小技术问题。
