---
layout: default
title: "Defensive Adversarial CAPTCHA: A Semantics-Driven Framework for Natural Adversarial Example Generation"
---

# Defensive Adversarial CAPTCHA: A Semantics-Driven Framework for Natural Adversarial Example Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10685" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10685v3</a>
  <a href="https://arxiv.org/pdf/2506.10685.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10685v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10685v3', 'Defensive Adversarial CAPTCHA: A Semantics-Driven Framework for Natural Adversarial Example Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xia Du, Xiaoyuan Liu, Jizhe Zhou, Zheng Lin, Chi-man Pun, Cong Wu, Tao Li, Zhe Chen, Wei Ni, Jun Luo

**分类**: cs.CV, cs.CR

**发布日期**: 2025-06-12 (更新: 2025-07-01)

**备注**: 13 pages, 6 figures

---

## 💡 一句话要点

**提出无源对抗CAPTCHA以解决传统CAPTCHA易受攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗样本生成` `深度学习安全` `CAPTCHA` `自然语言处理` `网络安全`

## 📋 核心要点

1. 核心问题：现有CAPTCHA方案易受到深度学习模型的攻击，导致安全性下降。
2. 方法要点：提出无源对抗CAPTCHA（DAC），通过语义信息生成高保真的对抗样本，增强CAPTCHA的多样性。
3. 实验或效果：BP-DAC生成的CAPTCHA能够有效抵御大多数未知模型，且对人类和DNN均不可区分。

## 📝 摘要（中文）

传统的CAPTCHA（完全自动化公共图灵测试）方案越来越容易受到深度神经网络（DNN）驱动的自动化攻击。现有的对抗攻击方法通常依赖于原始图像特征，导致产生的对抗样本难以被人类理解，并限制了在没有初始输入图像的场景中的适用性。为了解决这些挑战，本文提出了一种新颖的无源对抗CAPTCHA（DAC）框架，该框架通过攻击者指定的语义信息生成高保真对抗样本。通过利用大型语言模型（LLM），DAC增强了CAPTCHA的多样性并丰富了语义信息。实验表明，BP-DAC生成的防御性对抗CAPTCHA能够有效抵御大多数未知模型，并且生成的CAPTCHA对人类和DNN均不可区分。

## 🔬 方法详解

**问题定义**：本文旨在解决传统CAPTCHA在面对深度学习攻击时的脆弱性。现有方法往往依赖于原始图像特征，导致生成的对抗样本难以被人类理解，且在没有初始输入图像的情况下应用受限。

**核心思路**：提出无源对抗CAPTCHA（DAC）框架，通过攻击者指定的语义信息生成高保真对抗样本。利用大型语言模型（LLM）增强CAPTCHA的多样性和语义信息，从而提高对抗样本的有效性。

**技术框架**：DAC框架包含两个主要场景：白盒目标攻击和黑盒无目标攻击。对于目标攻击，引入两个潜在噪声变量，通过扩散步骤交替引导以实现稳健的反演；对于无目标攻击，采用双路径无源对抗CAPTCHA（BP-DAC），通过多模态梯度和双路径优化实现高效的误分类。

**关键创新**：最重要的创新在于结合了梯度引导和潜在变量优化，确保生成的对抗样本不仅符合目标条件，还在分布一致性和攻击有效性方面表现优异。这一方法与现有依赖原始图像特征的对抗攻击方法本质上不同。

**关键设计**：在目标攻击中，设计了两个潜在噪声变量的交替引导机制；在无目标攻击中，采用双路径优化策略，结合多模态梯度进行高效的误分类。

## 📊 实验亮点

实验结果表明，BP-DAC生成的防御性对抗CAPTCHA能够有效抵御大多数未知模型的攻击，且生成的CAPTCHA对人类和DNN均不可区分，显示出显著的安全性提升。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、用户身份验证和人机交互等。通过提高CAPTCHA的安全性和有效性，能够有效防止自动化攻击，保护用户信息安全。未来，该框架可能在其他对抗样本生成任务中展现出更广泛的应用价值。

## 📄 摘要（原文）

> Traditional CAPTCHA (Completely Automated Public Turing Test to Tell Computers and Humans Apart) schemes are increasingly vulnerable to automated attacks powered by deep neural networks (DNNs). Existing adversarial attack methods often rely on the original image characteristics, resulting in distortions that hinder human interpretation and limit their applicability in scenarios where no initial input images are available. To address these challenges, we propose the Unsourced Adversarial CAPTCHA (DAC), a novel framework that generates high-fidelity adversarial examples guided by attacker-specified semantics information. Leveraging a Large Language Model (LLM), DAC enhances CAPTCHA diversity and enriches the semantic information. To address various application scenarios, we examine the white-box targeted attack scenario and the black box untargeted attack scenario. For target attacks, we introduce two latent noise variables that are alternately guided in the diffusion step to achieve robust inversion. The synergy between gradient guidance and latent variable optimization achieved in this way ensures that the generated adversarial examples not only accurately align with the target conditions but also achieve optimal performance in terms of distributional consistency and attack effectiveness. In untargeted attacks, especially for black-box scenarios, we introduce bi-path unsourced adversarial CAPTCHA (BP-DAC), a two-step optimization strategy employing multimodal gradients and bi-path optimization for efficient misclassification. Experiments show that the defensive adversarial CAPTCHA generated by BP-DAC is able to defend against most of the unknown models, and the generated CAPTCHA is indistinguishable to both humans and DNNs.

