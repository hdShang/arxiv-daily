---
layout: default
title: SafeGenes: Evaluating the Adversarial Robustness of Genomic Foundation Models
---

# SafeGenes: Evaluating the Adversarial Robustness of Genomic Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00821" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00821v2</a>
  <a href="https://arxiv.org/pdf/2506.00821.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00821v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00821v2', 'SafeGenes: Evaluating the Adversarial Robustness of Genomic Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huixin Zhan, Clovis Barbour, Jason H. Moore

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-01 (更新: 2025-12-02)

---

## 💡 一句话要点

**提出SafeGenes框架以评估基因组基础模型的对抗鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基因组基础模型` `对抗攻击` `鲁棒性评估` `变异效应预测` `生物信息学` `深度学习` `安全性研究`

## 📋 核心要点

1. 现有基因组基础模型在对抗攻击下的鲁棒性尚未被充分研究，存在潜在的安全隐患。
2. SafeGenes框架通过结合FGSM和软提示攻击，全面评估基因组基础模型的对抗脆弱性。
3. 实验结果显示，针对浅层架构的攻击导致了显著的性能下降，揭示了基础模型的关键脆弱性。

## 📝 摘要（中文）

基因组基础模型（GFMs），如进化规模建模（ESM），在变异效应预测中取得了显著成功。然而，它们的对抗鲁棒性尚未得到充分探索。为了解决这一问题，本文提出了SafeGenes框架，通过对抗攻击评估GFMs的鲁棒性，包括针对近似对抗基因的攻击和嵌入空间的操控。我们使用快速梯度符号法（FGSM）和软提示攻击两种方法评估GFMs的对抗脆弱性。研究发现，针对MLM基础的浅层架构（如ProteinBERT）的软提示攻击导致了严重的性能下降，而在高容量基础模型（如ESM1b和ESM1v）中也出现了显著的失败模式。这些发现揭示了当前基础模型的关键脆弱性，为提高其在变异效应预测等高风险基因组应用中的安全性和鲁棒性开辟了新的研究方向。

## 🔬 方法详解

**问题定义**：本文旨在解决基因组基础模型（GFMs）在对抗攻击下的鲁棒性不足问题。现有方法未能充分评估其在面对对抗性输入时的脆弱性，可能导致在实际应用中的安全隐患。

**核心思路**：论文提出SafeGenes框架，通过对抗攻击评估GFMs的鲁棒性，结合了快速梯度符号法（FGSM）和软提示攻击，以全面分析模型的脆弱性。这样的设计旨在揭示模型在不同攻击方式下的表现差异。

**技术框架**：SafeGenes框架主要包括两个阶段：第一阶段使用FGSM对输入序列进行微小扰动，第二阶段通过优化连续嵌入进行软提示攻击，评估模型预测的变化。

**关键创新**：最重要的技术创新在于结合了两种不同的对抗攻击方法，提供了对GFMs脆弱性的全面评估。这种方法与传统的单一攻击方式相比，能够更深入地揭示模型的安全性问题。

**关键设计**：在实验中，FGSM通过引入最小扰动来影响输入，而软提示攻击则通过优化嵌入空间来操控模型预测，未直接修改输入标记。这些设计使得攻击更加隐蔽且有效。

## 📊 实验亮点

实验结果显示，针对ProteinBERT等浅层架构的软提示攻击导致了性能显著下降，表明其对抗鲁棒性不足。同时，即使在高容量模型如ESM1b和ESM1v中，仍然观察到明显的失败模式。这些结果强调了当前基础模型在实际应用中的脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括基因组数据分析、个性化医疗和生物信息学等。通过提高基因组基础模型的鲁棒性，SafeGenes框架能够在变异效应预测等高风险应用中提供更安全的解决方案，推动相关领域的研究和应用发展。

## 📄 摘要（原文）

> Genomic Foundation Models (GFMs), such as Evolutionary Scale Modeling (ESM), have demonstrated significant success in variant effect prediction. However, their adversarial robustness remains largely unexplored. To address this gap, we propose SafeGenes: a framework for Secure analysis of genomic foundation models, leveraging adversarial attacks to evaluate robustness against both engineered near-identical adversarial Genes and embedding-space manipulations. In this study, we assess the adversarial vulnerabilities of GFMs using two approaches: the Fast Gradient Sign Method (FGSM) and a soft prompt attack. FGSM introduces minimal perturbations to input sequences, while the soft prompt attack optimizes continuous embeddings to manipulate model predictions without modifying the input tokens. By combining these techniques, SafeGenes provides a comprehensive assessment of GFM susceptibility to adversarial manipulation. Targeted soft prompt attacks induced severe degradation in MLM-based shallow architectures such as ProteinBERT, while still producing substantial failure modes even in high-capacity foundation models such as ESM1b and ESM1v. These findings expose critical vulnerabilities in current foundation models, opening new research directions toward improving their security and robustness in high-stakes genomic applications such as variant effect prediction.

