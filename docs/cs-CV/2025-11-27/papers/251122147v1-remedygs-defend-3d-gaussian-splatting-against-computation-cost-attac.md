---
layout: default
title: RemedyGS: Defend 3D Gaussian Splatting against Computation Cost Attacks
---

# RemedyGS: Defend 3D Gaussian Splatting against Computation Cost Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22147" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22147v1</a>
  <a href="https://arxiv.org/pdf/2511.22147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22147v1" onclick="toggleFavorite(this, '2511.22147v1', 'RemedyGS: Defend 3D Gaussian Splatting against Computation Cost Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanping Li, Zhening Liu, Zijian Li, Zehong Lin, Jun Zhang

**分类**: cs.CV, cs.AI, cs.CR

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**提出RemedyGS框架，防御针对3D高斯溅射的计算成本攻击**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `计算成本攻击` `黑盒防御` `对抗训练` `图像净化`

## 📋 核心要点

1. 3D高斯溅射易受计算成本攻击，导致资源恶意占用甚至拒绝服务，阻碍其可靠部署。
2. RemedyGS框架通过检测和净化受攻击图像，并利用对抗训练对齐分布，实现有效防御。
3. 实验证明RemedyGS能有效防御多种攻击，并在安全性和效用上达到当前最佳水平。

## 📝 摘要（中文）

本文提出了一种有效且全面的黑盒防御框架RemedyGS，旨在防御针对3D高斯溅射（3DGS）的计算成本攻击，从而保护3DGS重建系统和服务。该框架包含两个关键组件：一个检测器，用于识别受污染纹理的攻击输入图像；以及一个净化器，用于从受攻击的图像中恢复良性图像，从而减轻这些攻击的不利影响。此外，我们将对抗训练融入到净化器中，以加强恢复图像和原始自然图像之间的分布对齐，从而提高防御效果。实验结果表明，我们的框架能够有效地防御3DGS系统中的白盒、黑盒和自适应攻击，在安全性和效用方面均实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决3D高斯溅射（3DGS）易受计算成本攻击的问题。这些攻击通过构造具有特定纹理的恶意输入图像，导致3DGS渲染过程消耗大量计算资源，从而造成拒绝服务（DoS）等问题。现有方法缺乏有效的黑盒防御机制，难以在实际部署中保护3DGS系统。

**核心思路**：RemedyGS的核心思路是构建一个黑盒防御框架，无需了解攻击的具体细节即可有效防御计算成本攻击。该框架通过检测受攻击的输入图像并将其净化为良性图像，从而减轻攻击的影响。同时，利用对抗训练来增强净化器的鲁棒性，使其能够更好地恢复图像的原始分布。

**技术框架**：RemedyGS框架主要包含两个模块：检测器和净化器。检测器负责识别输入图像是否受到攻击，可以采用各种异常检测方法。净化器则负责将受攻击的图像恢复为良性图像，可以使用图像修复或图像转换技术。对抗训练被用于优化净化器，使其生成的图像更接近原始自然图像的分布。

**关键创新**：RemedyGS的关键创新在于其黑盒防御特性和对抗训练的应用。与需要了解攻击细节的白盒防御方法不同，RemedyGS可以在不了解攻击方式的情况下进行防御，更具实用性。通过对抗训练，净化器能够更好地恢复图像的原始分布，从而提高防御效果。

**关键设计**：检测器可以使用预训练的图像分类模型或异常检测算法，例如基于自编码器的异常检测。净化器可以使用生成对抗网络（GAN）或变分自编码器（VAE）等模型，并采用对抗损失函数来鼓励生成的图像与原始图像分布对齐。对抗损失函数可以采用Wasserstein距离或KL散度等度量方式。具体的网络结构和参数设置需要根据实际情况进行调整。

## 📊 实验亮点

实验结果表明，RemedyGS能够有效防御白盒、黑盒和自适应攻击，在安全性和效用方面均优于现有方法。具体而言，RemedyGS在防御各种攻击时，能够显著降低计算资源的消耗，并保持较高的图像质量。与现有防御方法相比，RemedyGS在防御成功率和图像恢复质量方面均有显著提升。

## 🎯 应用场景

RemedyGS可广泛应用于各种基于3D高斯溅射的场景，例如三维重建、虚拟现实、增强现实、自动驾驶等。通过防御计算成本攻击，RemedyGS能够提高这些应用的稳定性和安全性，保障用户体验，并促进3DGS技术的可靠部署和广泛应用。该研究对于提升三维重建系统的安全性具有重要意义。

## 📄 摘要（原文）

> As a mainstream technique for 3D reconstruction, 3D Gaussian splatting (3DGS) has been applied in a wide range of applications and services. Recent studies have revealed critical vulnerabilities in this pipeline and introduced computation cost attacks that lead to malicious resource occupancies and even denial-of-service (DoS) conditions, thereby hindering the reliable deployment of 3DGS. In this paper, we propose the first effective and comprehensive black-box defense framework, named RemedyGS, against such computation cost attacks, safeguarding 3DGS reconstruction systems and services. Our pipeline comprises two key components: a detector to identify the attacked input images with poisoned textures and a purifier to recover the benign images from their attacked counterparts, mitigating the adverse effects of these attacks. Moreover, we incorporate adversarial training into the purifier to enforce distributional alignment between the recovered and original natural images, thereby enhancing the defense efficacy. Experimental results demonstrate that our framework effectively defends against white-box, black-box, and adaptive attacks in 3DGS systems, achieving state-of-the-art performance in both safety and utility.

