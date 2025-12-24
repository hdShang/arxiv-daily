---
layout: default
title: "DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device Large Language Models"
---

# DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09097" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09097v1</a>
  <a href="https://arxiv.org/pdf/2509.09097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09097v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09097v1', 'DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Honghui Xu, Shiva Shrestha, Wei Chen, Zhiyuan Li, Zhipeng Cai

**分类**: cs.CR, cs.AI

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**提出DP-FedLoRA，增强设备端LLM联邦微调的隐私保护。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `差分隐私` `大型语言模型` `设备端学习` `LoRA` `隐私保护` `模型微调`

## 📋 核心要点

1. 设备端LLM的联邦微调面临用户数据隐私泄露的挑战，现有方法难以在保护隐私的同时保持模型性能。
2. DP-FedLoRA框架结合LoRA和差分隐私，通过在本地裁剪和扰动LoRA矩阵，实现隐私保护的联邦微调。
3. 实验结果表明，DP-FedLoRA在主流基准测试中实现了有竞争力的性能，同时提供了强大的隐私保证。

## 📝 摘要（中文）

随着设备端大型语言模型（LLM）系统日益普及，联邦微调可以直接在边缘设备上实现高级语言理解和生成；然而，这也涉及到处理敏感的、用户特定的数据，从而在联邦学习框架内引发了严重的隐私问题。为了应对这些挑战，我们提出了一种隐私增强的联邦微调框架DP-FedLoRA，该框架集成了基于LoRA的适配与差分隐私，并具有通信效率。每个客户端在本地使用高斯噪声裁剪和扰动其LoRA矩阵，以满足($ε$, $δ$)-差分隐私。我们进一步提供了理论分析，证明了更新的无偏性，并推导了噪声引入的方差的界限，为隐私预算校准提供了实践指导。在主流基准测试上的实验结果表明，DP-FedLoRA在提供强大隐私保证的同时，实现了具有竞争力的性能，为设备端环境中可扩展且保护隐私的LLM部署铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决设备端联邦学习中，大型语言模型（LLM）微调过程中的隐私泄露问题。现有方法在联邦学习中直接共享模型参数或梯度，容易受到隐私攻击，尤其是在处理用户敏感数据时。如何在保护用户隐私的前提下，高效地进行LLM的联邦微调是一个关键挑战。

**核心思路**：论文的核心思路是将LoRA（Low-Rank Adaptation）与差分隐私（Differential Privacy）相结合。LoRA通过微调低秩矩阵来适应LLM，减少了需要传输的参数量，从而降低了通信成本。差分隐私则通过在本地添加噪声来保护用户数据的隐私。

**技术框架**：DP-FedLoRA框架包含以下主要步骤：1) 客户端在本地使用LoRA对LLM进行微调。2) 客户端对LoRA矩阵进行裁剪，限制其数值范围。3) 客户端向裁剪后的LoRA矩阵添加高斯噪声，以满足差分隐私。4) 客户端将添加噪声的LoRA矩阵上传到服务器。5) 服务器对接收到的LoRA矩阵进行聚合，更新全局模型。

**关键创新**：该方法最重要的创新点在于将LoRA与差分隐私相结合，在保证模型性能的同时，提供了强大的隐私保护。通过LoRA降低了需要保护的参数量，从而降低了差分隐私所需的噪声量，提高了模型性能。此外，论文还提供了理论分析，证明了更新的无偏性，并推导了噪声引入的方差的界限，为隐私预算校准提供了实践指导。

**关键设计**：关键设计包括：1) 使用高斯噪声实现差分隐私。2) 对LoRA矩阵进行裁剪，限制其数值范围，从而降低噪声的影响。3) 理论分析噪声对方差的影响，指导隐私预算的校准。4) 客户端本地微调时采用合适的学习率和迭代次数。

## 📊 实验亮点

实验结果表明，DP-FedLoRA在主流基准测试中实现了与非隐私保护方法具有竞争力的性能，同时提供了强大的隐私保证。具体来说，DP-FedLoRA在多个数据集上取得了接近甚至超过baseline的性能，同时满足了预设的差分隐私预算。

## 🎯 应用场景

DP-FedLoRA可应用于各种需要保护用户隐私的设备端LLM联邦微调场景，例如个性化推荐、智能助手、医疗诊断等。该研究有助于推动在边缘设备上部署可扩展且保护隐私的LLM，从而实现更安全、更智能的设备端应用。

## 📄 摘要（原文）

> As on-device large language model (LLM) systems become increasingly prevalent, federated fine-tuning enables advanced language understanding and generation directly on edge devices; however, it also involves processing sensitive, user-specific data, raising significant privacy concerns within the federated learning framework. To address these challenges, we propose DP-FedLoRA, a privacy-enhanced federated fine-tuning framework that integrates LoRA-based adaptation with differential privacy in a communication-efficient setting. Each client locally clips and perturbs its LoRA matrices using Gaussian noise to satisfy ($ε$, $δ$)-differential privacy. We further provide a theoretical analysis demonstrating the unbiased nature of the updates and deriving bounds on the variance introduced by noise, offering practical guidance for privacy-budget calibration. Experimental results across mainstream benchmarks show that DP-FedLoRA delivers competitive performance while offering strong privacy guarantees, paving the way for scalable and privacy-preserving LLM deployment in on-device environments.

