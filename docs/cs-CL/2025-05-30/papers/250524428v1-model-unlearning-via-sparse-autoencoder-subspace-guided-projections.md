---
layout: default
title: Model Unlearning via Sparse Autoencoder Subspace Guided Projections
---

# Model Unlearning via Sparse Autoencoder Subspace Guided Projections

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24428" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24428v1</a>
  <a href="https://arxiv.org/pdf/2505.24428.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24428v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24428v1', 'Model Unlearning via Sparse Autoencoder Subspace Guided Projections')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Wang, Zihao Li, Benyou Wang, Yan Hu, Difan Zou

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出SAE引导的子空间投影去学习方法以解决隐私问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `去学习` `稀疏自编码器` `子空间优化` `对抗鲁棒性` `隐私保护`

## 📋 核心要点

1. 现有的去学习方法在可解释性和对抗性防御方面存在不足，难以有效删除模型中的特定知识。
2. 论文提出的SSPU框架利用稀疏自编码器特征，通过子空间引导实现精确的模型参数更新，增强可解释性。
3. 实验结果表明，SSPU在减少有害知识准确率和提高对抗鲁棒性方面显著优于现有方法，展示了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）存储了大量信息，虽然其功能强大，但在需要选择性删除知识时引发了隐私和安全问题。现有的去学习策略，如基于梯度的微调和稀疏自编码器（SAE）引导，缺乏可解释性或未能有效抵御对抗性提示。我们提出了SAE引导的子空间投影去学习（SSPU）框架，利用SAE特征在模型参数空间中驱动有针对性的更新，实现精确、可解释和稳健的去学习。SSPU的三阶段流程包括数据驱动的层和特征选择、通过QR分解构建子空间，以及约束优化以控制激活进入“无关”子空间，同时保留已保留的知识。在WMDP-Cyber遗忘集和三个效用基准（MMLU、TruthfulQA、GSM8K）上的实验中，SSPU相比最强基线减少了3.22%的有害知识准确率，并提高了对抗鲁棒性，降低了在越狱提示下的恶意准确率。我们的研究揭示了先前去学习方法的局限性，并展示了可解释的子空间引导优化如何实现稳健、可控的模型行为。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型中选择性知识删除的挑战，现有方法在可解释性和对抗性防御方面存在明显不足。

**核心思路**：SSPU框架通过稀疏自编码器特征引导模型参数的有针对性更新，确保去学习过程的精确性和可解释性。

**技术框架**：SSPU的整体架构包括三个主要阶段：数据驱动的层和特征选择、QR分解构建子空间、以及约束优化以控制激活进入“无关”子空间，同时保留重要知识。

**关键创新**：SSPU的主要创新在于利用SAE特征构建一个监督去学习的子空间，通过优化损失函数和添加正则化项来引导可解释的参数更新，这与现有方法的设计理念有本质区别。

**关键设计**：在设计中，SSPU采用了特定的损失函数和正则化策略，以确保模型在去学习过程中保持稳定性和鲁棒性，同时通过优化算法控制参数更新的方向和幅度。

## 📊 实验亮点

实验结果显示，SSPU在WMDP-Cyber遗忘集上相比最强基线减少了3.22%的有害知识准确率，并在对抗性测试中显著降低了恶意准确率，展示了其在稳健性和可解释性方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括需要保护用户隐私的场景，如社交媒体、在线服务和医疗数据管理。通过提供一种可控的去学习机制，SSPU能够帮助企业在遵循数据隐私法规的同时，保持模型的有效性和安全性。未来，该方法可能在更多领域得到推广，促进AI系统的透明性和信任度。

## 📄 摘要（原文）

> Large language models (LLMs) store vast amounts of information, making them powerful yet raising privacy and safety concerns when selective knowledge removal is required. Existing unlearning strategies, ranging from gradient-based fine-tuning and model editing to sparse autoencoder (SAE) steering, either lack interpretability or fail to provide a robust defense against adversarial prompts. We propose SAE-Guided Subspace Projection Unlearning (SSPU), a novel framework that leverages SAE features to drive targeted updates in the model's parameter space, enabling precise, interpretable, and robust unlearning. SSPU's three-stage pipeline performs data-driven layer and feature selection, subspace construction via QR decomposition, and constrained optimization that controls activations into an "irrelevant" subspace while preserving retained knowledge. Overall, we use SAE features to construct a subspace that supervises unlearning, refining the loss and adding a regularization term to guide interpretable parameter updates. In experiments on the WMDP-Cyber forget set and three utility benchmarks (MMLU, TruthfulQA, GSM8K), SSPU reduces harmful knowledge accuracy by 3.22% compared to the strongest baseline. It also improves adversarial robustness, lowering malicious accuracy under jailbreak prompts compared to baselines. Our findings expose the limitations of prior unlearning methods and demonstrate how interpretable subspace-guided optimization can achieve robust, controllable model behavior.

