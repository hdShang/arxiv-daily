---
layout: default
title: Perfect reconstruction of sparse signals using nonconvexity control and one-step RSB message passing
---

# Perfect reconstruction of sparse signals using nonconvexity control and one-step RSB message passing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17426" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17426v1</a>
  <a href="https://arxiv.org/pdf/2512.17426.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17426v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17426v1', 'Perfect reconstruction of sparse signals using nonconvexity control and one-step RSB message passing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaosi Gu, Ayaka Sakata, Tomoyuki Obuchi

**分类**: stat.ML, cond-mat.dis-nn, cs.LG

**发布日期**: 2025-12-19

**备注**: 49 pages, 10 figures

---

## 💡 一句话要点

**提出基于非凸性控制和一步RSB消息传递的稀疏信号完美重构方法**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `稀疏信号重构` `近似消息传递` `副本对称性破缺` `非凸性控制` `SCAD惩罚`

## 📋 核心要点

1. 现有基于副本对称（RS）的近似消息传递（AMP）方法在稀疏信号重构中存在算法极限，无法达到贝叶斯最优。
2. 本文提出一步副本对称性破缺（1RSB）的AMP扩展，并结合非凸性控制（NCC）协议，旨在提升稀疏信号完美重构的算法极限。
3. 实验结果表明，与RS-AMP相比，该方法提高了完美重构的算法极限，尽管提升幅度有限，且仍略低于贝叶斯最优阈值。

## 📝 摘要（中文）

本文研究了通过最小化平滑裁剪绝对偏差（SCAD）惩罚进行稀疏信号重构的问题，并开发了近似消息传递（AMP）的一步副本对称性破缺（1RSB）扩展，称为1RSB-AMP。从置信传播的1RSB公式出发，我们推导了1RSB-AMP的显式更新规则以及相应的状态演化（1RSB-SE）方程。详细的比较表明，1RSB-AMP和1RSB-SE在宏观层面上非常吻合，即使在副本对称（RS）AMP（称为RS-AMP）发散的参数区域以及1RSB描述本身预计在热力学上不精确的区域也是如此。1RSB-SE的定点分析揭示了一个由成功、失败和发散阶段组成的状态图，与RS情况相同。然而，由于1RSB ansatz，发散区域边界现在取决于Parisi参数，我们提出了一种新的标准——最小化发散区域的大小——而不是传统的零复杂度条件，来确定其值。将此标准与先前RS研究中提出的非凸性控制（NCC）协议相结合，与RS-AMP相比，提高了完美重构的算法极限。1RSB-SE的数值解和1RSB-AMP的实验证实，实际上实现了这一改进的极限，尽管增益不大，并且仍然略低于贝叶斯最优阈值。我们还报告了热力学量的行为——重叠、自由熵、复杂性和非自平均磁化率——这些量表征了该问题中的1RSB阶段。

## 🔬 方法详解

**问题定义**：论文旨在解决稀疏信号重构问题，具体而言，是通过最小化SCAD惩罚函数来实现。现有基于RS-AMP的方法在某些参数区域会发散，且算法极限距离贝叶斯最优阈值仍有差距，这意味着重构性能有待提升。

**核心思路**：论文的核心思路是引入一步副本对称性破缺（1RSB）框架，对AMP算法进行扩展。1RSB框架能够更准确地描述系统的复杂性，从而改善算法的性能。此外，结合非凸性控制（NCC）协议，进一步优化算法的性能。

**技术框架**：整体框架包括以下几个主要步骤：1）从置信传播的1RSB公式出发，推导1RSB-AMP的更新规则；2）建立相应的状态演化（1RSB-SE）方程；3）通过定点分析，得到包含成功、失败和发散阶段的状态图；4）提出最小化发散区域大小的新标准来确定Parisi参数；5）结合NCC协议，优化算法性能。

**关键创新**：最重要的技术创新点在于将1RSB框架引入到AMP算法中，并提出了一种新的确定Parisi参数的标准，即最小化发散区域的大小。与传统的零复杂度条件相比，该标准能够更有效地控制算法的发散行为，从而提高重构性能。

**关键设计**：论文的关键设计包括：1）SCAD惩罚函数的选择，它是一种非凸惩罚函数，能够更好地促进稀疏性；2）1RSB-AMP的更新规则，这些规则基于置信传播的1RSB公式推导而来；3）NCC协议的具体实现，它通过控制非凸性来优化算法的性能；4）Parisi参数的确定方法，即最小化发散区域的大小。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17426v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17426v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17426v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，与RS-AMP相比，1RSB-AMP结合NCC协议提高了完美重构的算法极限。虽然提升幅度有限，且仍略低于贝叶斯最优阈值，但验证了1RSB框架在稀疏信号重构中的有效性。数值解和实验结果在宏观层面上高度吻合，验证了理论分析的正确性。

## 🎯 应用场景

该研究成果可应用于压缩感知、图像处理、无线通信等领域，在这些领域中，稀疏信号重构是一个关键问题。通过提高稀疏信号重构的性能，可以改善这些应用的效果，例如，在压缩感知中，可以减少所需的采样数量，在图像处理中，可以提高图像的重建质量。

## 📄 摘要（原文）

> We consider sparse signal reconstruction via minimization of the smoothly clipped absolute deviation (SCAD) penalty, and develop one-step replica-symmetry-breaking (1RSB) extensions of approximate message passing (AMP), termed 1RSB-AMP. Starting from the 1RSB formulation of belief propagation, we derive explicit update rules of 1RSB-AMP together with the corresponding state evolution (1RSB-SE) equations. A detailed comparison shows that 1RSB-AMP and 1RSB-SE agree remarkably well at the macroscopic level, even in parameter regions where replica-symmetric (RS) AMP, termed RS-AMP, diverges and where the 1RSB description itself is not expected to be thermodynamically exact. Fixed-point analysis of 1RSB-SE reveals a phase diagram consisting of success, failure, and diverging phases, as in the RS case. However, the diverging-region boundary now depends on the Parisi parameter due to the 1RSB ansatz, and we propose a new criterion -- minimizing the size of the diverging region -- rather than the conventional zero-complexity condition, to determine its value. Combining this criterion with the nonconvexity-control (NCC) protocol proposed in a previous RS study improves the algorithmic limit of perfect reconstruction compared with RS-AMP. Numerical solutions of 1RSB-SE and experiments with 1RSB-AMP confirm that this improved limit is achieved in practice, though the gain is modest and remains slightly inferior to the Bayes-optimal threshold. We also report the behavior of thermodynamic quantities -- overlaps, free entropy, complexity, and the non-self-averaging susceptibility -- that characterize the 1RSB phase in this problem.

