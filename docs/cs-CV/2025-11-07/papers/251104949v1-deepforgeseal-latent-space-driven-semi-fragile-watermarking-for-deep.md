---
layout: default
title: DeepForgeSeal: Latent Space-Driven Semi-Fragile Watermarking for Deepfake Detection Using Multi-Agent Adversarial Reinforcement Learning
---

# DeepForgeSeal: Latent Space-Driven Semi-Fragile Watermarking for Deepfake Detection Using Multi-Agent Adversarial Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04949" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04949v1</a>
  <a href="https://arxiv.org/pdf/2511.04949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04949v1" onclick="toggleFavorite(this, '2511.04949v1', 'DeepForgeSeal: Latent Space-Driven Semi-Fragile Watermarking for Deepfake Detection Using Multi-Agent Adversarial Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tharindu Fernando, Clinton Fookes, Sridha Sridharan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-07

---

## 💡 一句话要点

**提出DeepForgeSeal，利用潜空间水印和对抗强化学习进行深度伪造检测。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度伪造检测` `水印技术` `潜空间嵌入` `对抗强化学习` `多智能体系统`

## 📋 核心要点

1. 现有被动深度伪造检测器依赖特定伪造痕迹，泛化能力不足，难以应对新型深度伪造。
2. 提出DeepForgeSeal，利用潜空间水印嵌入和多智能体对抗强化学习，实现鲁棒且自适应的水印方案。
3. 在CelebA和CelebA-HQ数据集上，该方法优于现有技术，性能分别提升超过4.5%和5.3%。

## 📝 摘要（中文）

生成式AI的快速发展导致深度伪造技术日益逼真，对执法部门和公众信任构成严峻挑战。现有的被动深度伪造检测器难以跟上步伐，主要原因是它们依赖于特定的伪造痕迹，这限制了它们对新型深度伪造的泛化能力。主动式深度伪造检测（即水印技术）应运而生，旨在识别高质量的合成媒体。然而，这些方法通常难以在抵抗良性失真和对恶意篡改的敏感性之间取得平衡。本文提出了一种新颖的深度学习框架，该框架利用高维潜在空间表示和多智能体对抗强化学习（MAARL）范式来开发一种鲁棒且自适应的水印方法。具体来说，我们开发了一种可学习的水印嵌入器，它在潜在空间中运行，捕获高级图像语义，同时提供对消息编码和提取的精确控制。MAARL范式使可学习的水印代理能够通过与对抗攻击者代理模拟的良性和恶意图像操作的动态课程进行交互，从而追求鲁棒性和脆弱性之间的最佳平衡。在CelebA和CelebA-HQ基准上的全面评估表明，我们的方法始终优于最先进的方法，在具有挑战性的操作场景下，在CelebA上实现了超过4.5%的改进，在CelebA-HQ上实现了超过5.3%的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决深度伪造检测中，现有被动检测方法泛化性差，以及主动水印方法鲁棒性和脆弱性难以平衡的问题。现有方法依赖于特定的伪造痕迹，无法有效检测新型深度伪造，而传统水印方法在抵抗良性失真的同时，难以对恶意篡改保持敏感。

**核心思路**：论文的核心思路是利用深度学习在图像的潜在空间中嵌入水印，并使用多智能体对抗强化学习（MAARL）来训练水印嵌入器，使其在鲁棒性和脆弱性之间达到最佳平衡。通过在潜空间操作，可以更好地捕获图像的语义信息，从而提高水印的鲁棒性。MAARL则允许水印嵌入器通过与对抗攻击者交互，学习适应各种攻击，从而提高水印的自适应性。

**技术框架**：整体框架包含一个可学习的水印嵌入器和一个对抗攻击者。水印嵌入器负责在图像的潜在空间中嵌入水印，而对抗攻击者则模拟各种良性和恶意的图像操作，试图破坏水印。这两个智能体通过强化学习进行训练，水印嵌入器的目标是最大化水印的鲁棒性和脆弱性，而对抗攻击者的目标是最小化水印的鲁棒性。训练过程采用动态课程学习，逐渐增加攻击的难度，以提高水印的泛化能力。

**关键创新**：该方法最重要的创新点在于将潜空间水印嵌入和多智能体对抗强化学习相结合。潜空间水印嵌入可以更好地捕获图像的语义信息，提高水印的鲁棒性。MAARL则允许水印嵌入器通过与对抗攻击者交互，学习适应各种攻击，从而提高水印的自适应性。这种结合使得该方法能够在鲁棒性和脆弱性之间达到更好的平衡。

**关键设计**：水印嵌入器通常是一个深度神经网络，例如自编码器或生成对抗网络（GAN）。对抗攻击者也可以是一个深度神经网络，用于模拟各种图像操作，例如添加噪声、模糊、裁剪、旋转等。损失函数的设计至关重要，需要同时考虑水印的鲁棒性和脆弱性。常用的损失函数包括水印提取的准确率、图像质量的损失、以及对抗攻击的损失。参数设置方面，需要仔细调整学习率、批量大小、以及强化学习中的奖励函数等。

## 📊 实验亮点

实验结果表明，DeepForgeSeal在CelebA和CelebA-HQ数据集上均优于现有技术，在具有挑战性的操作场景下，CelebA上实现了超过4.5%的改进，CelebA-HQ上实现了超过5.3%的改进。这表明该方法在鲁棒性和脆弱性之间取得了更好的平衡，能够有效抵抗各种攻击，同时对恶意篡改保持敏感。

## 🎯 应用场景

该研究成果可应用于数字媒体版权保护、深度伪造内容溯源、以及信息安全等领域。通过在图像或视频中嵌入半脆弱水印，可以验证内容的真实性和完整性，从而打击深度伪造和虚假信息传播。该技术还可以用于保护知识产权，防止未经授权的复制和传播。

## 📄 摘要（原文）

> Rapid advances in generative AI have led to increasingly realistic deepfakes, posing growing challenges for law enforcement and public trust. Existing passive deepfake detectors struggle to keep pace, largely due to their dependence on specific forgery artifacts, which limits their ability to generalize to new deepfake types. Proactive deepfake detection using watermarks has emerged to address the challenge of identifying high-quality synthetic media. However, these methods often struggle to balance robustness against benign distortions with sensitivity to malicious tampering. This paper introduces a novel deep learning framework that harnesses high-dimensional latent space representations and the Multi-Agent Adversarial Reinforcement Learning (MAARL) paradigm to develop a robust and adaptive watermarking approach. Specifically, we develop a learnable watermark embedder that operates in the latent space, capturing high-level image semantics, while offering precise control over message encoding and extraction. The MAARL paradigm empowers the learnable watermarking agent to pursue an optimal balance between robustness and fragility by interacting with a dynamic curriculum of benign and malicious image manipulations simulated by an adversarial attacker agent. Comprehensive evaluations on the CelebA and CelebA-HQ benchmarks reveal that our method consistently outperforms state-of-the-art approaches, achieving improvements of over 4.5% on CelebA and more than 5.3% on CelebA-HQ under challenging manipulation scenarios.

