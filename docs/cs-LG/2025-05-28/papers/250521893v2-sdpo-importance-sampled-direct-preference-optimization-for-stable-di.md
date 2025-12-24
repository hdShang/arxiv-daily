---
layout: default
title: "SDPO: Importance-Sampled Direct Preference Optimization for Stable Diffusion Training"
---

# SDPO: Importance-Sampled Direct Preference Optimization for Stable Diffusion Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21893" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21893v2</a>
  <a href="https://arxiv.org/pdf/2505.21893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21893v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21893v2', 'SDPO: Importance-Sampled Direct Preference Optimization for Stable Diffusion Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaomeng Yang, Zhiyu Tan, Junyan Wang, Zhijian Zhou, Hao Li

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-28 (更新: 2025-09-25)

**备注**: This version contains a critical error in the main theorem and proof design that affects the validity of the results

---

## 💡 一句话要点

**提出SDPO以解决扩散模型训练中的偏差和不稳定问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `偏好学习` `重要性采样` `训练稳定性` `生成模型`

## 📋 核心要点

1. 现有的Diffusion-DPO方法在训练过程中面临时间步依赖的不稳定性和离策略偏差等挑战。
2. 本文提出DPO-C&M策略，通过剪切和屏蔽无信息时间步来改善稳定性，并引入SDPO框架以纠正离策略偏差。
3. 实验结果显示，SDPO在多个基准上超越了标准Diffusion-DPO，表现出更好的偏好对齐和训练鲁棒性。

## 📝 摘要（中文）

偏好学习已成为对齐生成模型与人类期望的核心技术，最近通过直接偏好优化（DPO）扩展到扩散模型。然而，现有方法如Diffusion-DPO面临两个主要挑战：时间步依赖的不稳定性和由优化与数据收集策略不匹配引起的离策略偏差。本文分析了反向扩散轨迹，发现不稳定性主要发生在低重要性权重的早期时间步。为了解决这些问题，提出了DPO-C&M策略，通过剪切和屏蔽无信息时间步来改善稳定性，同时部分缓解离策略偏差。在此基础上，提出了SDPO（重要性采样直接偏好优化），这是一个将重要性采样纳入目标的原则性框架，旨在完全纠正离策略偏差并强调扩散过程中的信息更新。实验结果表明，SDPO在VBench评分、人类偏好对齐和训练鲁棒性方面均优于标准Diffusion-DPO。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型训练中的不稳定性和离策略偏差问题。现有的Diffusion-DPO方法在早期时间步表现出高梯度方差和不匹配的优化策略，导致训练效果不佳。

**核心思路**：通过分析反向扩散轨迹，发现不稳定性主要集中在低重要性权重的早期时间步。提出DPO-C&M策略以改善稳定性，并在此基础上引入SDPO框架，利用重要性采样来纠正离策略偏差。

**技术框架**：SDPO框架包括两个主要模块：一是DPO-C&M策略用于稳定训练，二是重要性采样机制用于优化目标，强调信息更新。整体流程从数据收集到优化目标再到模型更新，确保每一步都能有效对齐人类偏好。

**关键创新**：SDPO的核心创新在于将重要性采样引入偏好优化中，完全纠正了离策略偏差，强调了信息更新的有效性。这与现有方法的本质区别在于其对时间步的敏感性和优化策略的调整。

**关键设计**：在SDPO中，重要性权重的计算和时间步的选择是关键设计因素。损失函数经过调整，以确保在训练过程中对重要时间步的更新给予更多关注，同时采用了剪切和屏蔽策略以提高训练的稳定性。

## 📊 实验亮点

实验结果表明，SDPO在VBench评分上显著优于标准Diffusion-DPO，具体提升幅度达到X%（具体数据未知）。此外，SDPO在与人类偏好的对齐和训练鲁棒性方面也表现出更好的性能，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括生成模型的训练、视频生成、图像合成等。通过提高扩散模型的训练稳定性和对人类偏好的对齐能力，SDPO能够在实际生成任务中提供更高质量的输出，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Preference learning has become a central technique for aligning generative models with human expectations. Recently, it has been extended to diffusion models through methods like Direct Preference Optimization (DPO). However, existing approaches such as Diffusion-DPO suffer from two key challenges: timestep-dependent instability, caused by a mismatch between the reverse and forward diffusion processes and by high gradient variance in early noisy timesteps, and off-policy bias arising from the mismatch between optimization and data collection policies. We begin by analyzing the reverse diffusion trajectory and observe that instability primarily occurs at early timesteps with low importance weights. To address these issues, we first propose DPO-C\&M, a practical strategy that improves stability by clipping and masking uninformative timesteps while partially mitigating off-policy bias. Building on this, we introduce SDPO (Importance-Sampled Direct Preference Optimization), a principled framework that incorporates importance sampling into the objective to fully correct for off-policy bias and emphasize informative updates during the diffusion process. Experiments on CogVideoX-2B, CogVideoX-5B, and Wan2.1-1.3B demonstrate that both methods outperform standard Diffusion-DPO, with SDPO achieving superior VBench scores, human preference alignment, and training robustness. These results highlight the importance of timestep-aware, distribution-corrected optimization in diffusion-based preference learning.

