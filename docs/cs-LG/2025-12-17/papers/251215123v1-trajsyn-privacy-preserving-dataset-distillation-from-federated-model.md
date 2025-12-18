---
layout: default
title: TrajSyn: Privacy-Preserving Dataset Distillation from Federated Model Trajectories for Server-Side Adversarial Training
---

# TrajSyn: Privacy-Preserving Dataset Distillation from Federated Model Trajectories for Server-Side Adversarial Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15123" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15123v1</a>
  <a href="https://arxiv.org/pdf/2512.15123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15123v1" onclick="toggleFavorite(this, '2512.15123v1', 'TrajSyn: Privacy-Preserving Dataset Distillation from Federated Model Trajectories for Server-Side Adversarial Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mukur Gupta, Niharika Gupta, Saifur Rahman, Shantanu Pal, Chandan Karmakar

**分类**: cs.LG

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**TrajSyn：联邦学习中基于模型轨迹的隐私保护数据集蒸馏，用于服务端对抗训练**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `联邦学习` `对抗训练` `隐私保护` `数据集蒸馏` `模型轨迹`

## 📋 核心要点

1. 联邦学习中的对抗训练面临客户端数据隐私和边缘设备计算资源有限的双重挑战。
2. TrajSyn通过分析客户端模型更新轨迹，在服务端合成代理数据集，用于对抗训练，无需访问原始数据。
3. 实验结果表明，TrajSyn在图像分类任务上有效提升了模型的对抗鲁棒性，且不增加客户端计算负担。

## 📝 摘要（中文）

深度学习模型在边缘设备上的部署日益广泛，尤其是在安全攸关的应用中。然而，它们对对抗扰动的脆弱性带来了显著风险，特别是在联邦学习（FL）环境中，相同的模型分布在成千上万的客户端上。虽然对抗训练是一种强大的防御手段，但由于严格的客户端数据隐私约束和边缘设备上有限的计算资源，它很难在FL中应用。本文提出了TrajSyn，一个隐私保护框架，它通过从客户端模型更新的轨迹中合成代理数据集，从而实现有效的服务端对抗训练，而无需访问原始客户端数据。实验表明，TrajSyn在图像分类基准测试中持续提高对抗鲁棒性，且不会给客户端设备带来额外的计算负担。

## 🔬 方法详解

**问题定义**：联邦学习场景下，直接在客户端进行对抗训练会暴露用户隐私，而服务端缺乏对抗样本。现有方法难以在保护客户端数据隐私的同时，提升联邦学习模型的对抗鲁棒性。

**核心思路**：TrajSyn的核心思想是从客户端模型更新的轨迹中提取信息，生成一个具有代表性的代理数据集，该数据集能够模拟真实客户端数据的分布，从而在服务端进行有效的对抗训练，而无需访问原始客户端数据。

**技术框架**：TrajSyn框架主要包含以下几个阶段：1) 客户端模型训练：每个客户端使用本地数据训练模型，并将模型更新发送到服务器。2) 模型轨迹收集：服务器收集来自不同客户端的模型更新轨迹。3) 代理数据集生成：服务器利用收集到的模型轨迹，通过某种生成机制（例如，生成对抗网络或变分自编码器）合成一个代理数据集。4) 服务端对抗训练：服务器使用生成的代理数据集对全局模型进行对抗训练，提高模型的鲁棒性。

**关键创新**：TrajSyn的关键创新在于利用模型更新轨迹作为隐私保护的信息源，从而在服务端合成代理数据集，用于对抗训练。与直接共享客户端数据或使用差分隐私等方法相比，TrajSyn在隐私保护和模型性能之间取得了更好的平衡。

**关键设计**：TrajSyn的关键设计包括：1) 如何有效地从模型轨迹中提取信息，以生成具有代表性的代理数据集。这可能涉及到设计特定的损失函数，以确保代理数据集能够捕捉到真实数据的关键特征。2) 如何选择合适的生成模型，例如GAN或VAE，以及如何调整其参数，以生成高质量的代理数据集。3) 对抗训练的具体方法，例如选择合适的对抗攻击算法和对抗训练策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15123v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15123v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了TrajSyn在图像分类任务上的有效性。实验结果表明，TrajSyn能够在不增加客户端计算负担的情况下，显著提高模型的对抗鲁棒性。具体的性能数据和对比基线（例如，未进行对抗训练的模型）的提升幅度需要在论文中查找。

## 🎯 应用场景

TrajSyn适用于各种联邦学习场景，尤其是在数据隐私至关重要的领域，如医疗保健、金融和自动驾驶。它能够提升联邦学习模型的安全性，使其免受对抗攻击，从而提高系统的可靠性和安全性。未来，TrajSyn可以扩展到更复杂的模型和数据集，并与其他隐私保护技术相结合，以实现更强大的隐私保护和模型性能。

## 📄 摘要（原文）

> Deep learning models deployed on edge devices are increasingly used in safety-critical applications. However, their vulnerability to adversarial perturbations poses significant risks, especially in Federated Learning (FL) settings where identical models are distributed across thousands of clients. While adversarial training is a strong defense, it is difficult to apply in FL due to strict client-data privacy constraints and the limited compute available on edge devices. In this work, we introduce TrajSyn, a privacy-preserving framework that enables effective server-side adversarial training by synthesizing a proxy dataset from the trajectories of client model updates, without accessing raw client data. We show that TrajSyn consistently improves adversarial robustness on image classification benchmarks with no extra compute burden on the client device.

