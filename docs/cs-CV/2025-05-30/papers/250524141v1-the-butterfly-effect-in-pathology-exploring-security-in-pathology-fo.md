---
layout: default
title: The Butterfly Effect in Pathology: Exploring Security in Pathology Foundation Models
---

# The Butterfly Effect in Pathology: Exploring Security in Pathology Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24141" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24141v1</a>
  <a href="https://arxiv.org/pdf/2505.24141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24141v1', 'The Butterfly Effect in Pathology: Exploring Security in Pathology Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiashuai Liu, Yingjia Shang, Yingkang Zhan, Di Zhang, Yi Niu, Dong Wei, Xian Wu, Zeyu Gao, Chen Li, Yefeng Zheng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-30

**🔗 代码/项目**: [GITHUB](https://github.com/Jiashuai-Liu-hmos/Attack-WSI-pathology-foundation-models)

---

## 💡 一句话要点

**提出局部扰动与全球影响原则以提升病理模型安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理学` `对抗攻击` `模型安全性` `全幻灯片图像` `无标签攻击` `深度学习` `医疗影像分析`

## 📋 核心要点

1. 现有病理基础模型在面对对抗攻击时的脆弱性尚未得到充分研究，安全性问题亟待解决。
2. 本文提出了一种基于局部扰动与全球影响原则的无标签攻击框架，旨在增强病理模型的安全性。
3. 实验结果表明，攻击仅需修改0.1%的补丁即可导致下游任务准确率下降高达20%，显示出模型的脆弱性。

## 📝 摘要（中文）

随着病理基础模型在研究和临床决策支持系统中的广泛应用，探索其安全性成为关键问题。然而，尽管其影响日益增长，这些模型对对抗攻击的脆弱性仍未得到充分研究。本文首次系统性地调查了病理基础模型在全幻灯片图像分析中的安全性，提出了一种无需访问下游任务标签的无标签攻击框架。通过对四种经典白盒攻击方法的修订，并根据全幻灯片图像的特性重新定义扰动预算，我们在三个代表性病理基础模型上进行了全面实验，结果显示，尽管仅修改了每张幻灯片0.1%的补丁，攻击导致的下游准确率下降在最坏情况下可达20%。

## 🔬 方法详解

**问题定义**：本文旨在解决病理基础模型在全幻灯片图像分析中对抗攻击的脆弱性问题。现有方法未能充分考虑模型在实际应用中的安全性，导致其易受攻击。

**核心思路**：论文提出的无标签攻击框架基于局部扰动与全球影响的原则，允许在不依赖下游任务标签的情况下进行有效攻击，从而提高攻击的隐蔽性和有效性。

**技术框架**：整体架构包括攻击框架的设计、扰动预算的重新定义以及对四种经典白盒攻击方法的修订。主要模块包括数据预处理、攻击实施和结果评估。

**关键创新**：最重要的技术创新在于提出了局部扰动与全球影响的原则，并在此基础上设计了无标签攻击框架，这与传统方法依赖标签的方式有本质区别。

**关键设计**：在攻击实施中，论文重新定义了扰动预算，针对全幻灯片图像的特性进行了优化，确保即使是微小的扰动也能显著影响模型的输出。

## 📊 实验亮点

实验结果显示，尽管仅对每张幻灯片的0.1%补丁施加不可察觉的噪声，攻击仍能导致下游任务准确率下降高达20%。这一发现强调了病理基础模型在实际应用中的脆弱性，为未来的防御策略提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括医疗图像分析、病理学诊断和人工智能辅助医疗决策。通过提高病理基础模型的安全性，可以增强其在临床环境中的可靠性，降低因对抗攻击导致的误诊风险，进而提升患者的安全性和治疗效果。

## 📄 摘要（原文）

> With the widespread adoption of pathology foundation models in both research and clinical decision support systems, exploring their security has become a critical concern. However, despite their growing impact, the vulnerability of these models to adversarial attacks remains largely unexplored. In this work, we present the first systematic investigation into the security of pathology foundation models for whole slide image~(WSI) analysis against adversarial attacks. Specifically, we introduce the principle of \textit{local perturbation with global impact} and propose a label-free attack framework that operates without requiring access to downstream task labels. Under this attack framework, we revise four classical white-box attack methods and redefine the perturbation budget based on the characteristics of WSI. We conduct comprehensive experiments on three representative pathology foundation models across five datasets and six downstream tasks. Despite modifying only 0.1\% of patches per slide with imperceptible noise, our attack leads to downstream accuracy degradation that can reach up to 20\% in the worst cases. Furthermore, we analyze key factors that influence attack success, explore the relationship between patch-level vulnerability and semantic content, and conduct a preliminary investigation into potential defence strategies. These findings lay the groundwork for future research on the adversarial robustness and reliable deployment of pathology foundation models. Our code is publicly available at: https://github.com/Jiashuai-Liu-hmos/Attack-WSI-pathology-foundation-models.

