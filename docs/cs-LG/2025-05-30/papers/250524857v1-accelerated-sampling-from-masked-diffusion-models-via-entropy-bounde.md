---
layout: default
title: Accelerated Sampling from Masked Diffusion Models via Entropy Bounded Unmasking
---

# Accelerated Sampling from Masked Diffusion Models via Entropy Bounded Unmasking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24857" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24857v1</a>
  <a href="https://arxiv.org/pdf/2505.24857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24857v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24857v1', 'Accelerated Sampling from Masked Diffusion Models via Entropy Bounded Unmasking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heli Ben-Hamu, Itai Gat, Daniel Severo, Niklas Nolte, Brian Karrer

**分类**: cs.LG

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出EB-Sampler以加速从掩蔽扩散模型的采样**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `掩蔽扩散模型` `高效采样` `熵有界解掩蔽` `自然语言处理` `智能推理`

## 📋 核心要点

1. 现有的掩蔽扩散模型在采样效率上存在不足，尤其是在处理部分掩蔽序列时未能充分利用信息。
2. 论文提出EB-Sampler，通过熵有界的解掩蔽方法，能够在一次评估中解掩蔽多个标记，提高采样效率。
3. 实验结果表明，EB-Sampler在标准基准上加速采样2-3倍，同时在小型推理任务中也表现出色。

## 📝 摘要（中文）

近期的掩蔽扩散模型（MDMs）在语言建模方面表现出色，但高效采样的研究相对较少。本文观察到，部分掩蔽的序列可以确定多个未知标记的值，因此单次预测包含未被标准采样程序利用的额外信息。基于此，提出了EB-Sampler，这是一种简单的替代现有采样器的方法，利用熵有界的解掩蔽程序，在一次函数评估中动态解掩蔽多个标记，并设定了近似误差容忍度。EB-Sampler在标准编码和数学推理基准上加速采样速度约2-3倍，且性能无损，同时在迷宫导航和数独等较小推理任务中也表现良好。

## 🔬 方法详解

**问题定义**：本文旨在解决从掩蔽扩散模型中高效采样的问题。现有方法在处理部分掩蔽序列时，未能充分利用单次预测所包含的额外信息，导致采样效率低下。

**核心思路**：论文的核心思路是通过熵有界的解掩蔽程序，动态解掩蔽多个标记，从而在一次函数评估中提高采样效率。这样的设计能够充分利用部分掩蔽序列所蕴含的信息，减少采样所需的计算量。

**技术框架**：EB-Sampler的整体架构包括输入部分掩蔽序列、熵有界解掩蔽模块和输出解掩蔽结果。该框架允许在一次评估中同时解掩蔽多个标记，提升了采样速度。

**关键创新**：EB-Sampler的主要创新在于其熵有界的解掩蔽机制，能够在保持性能的同时显著提高采样速度。这一方法与现有的逐步采样方法本质上不同，后者通常只关注单个标记的预测。

**关键设计**：EB-Sampler的设计中，设定了近似误差容忍度，以确保在解掩蔽过程中不会损失重要信息。此外，模块的参数设置和损失函数设计也经过精心调整，以优化整体性能。

## 📊 实验亮点

实验结果显示，EB-Sampler在标准编码和数学推理基准上加速采样速度约2-3倍，且在小型推理任务如迷宫导航和数独中表现良好，展现出较强的适应性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和自动化推理等。通过提高掩蔽扩散模型的采样效率，EB-Sampler能够在实际应用中实现更快的响应时间和更高的处理能力，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent masked diffusion models (MDMs) have shown competitive performance compared to autoregressive models (ARMs) for language modeling. While most literature has focused on performance enhancing sampling procedures, efficient sampling from MDMs has been scarcely explored. We make the observation that often a given sequence of partially masked tokens determines the values of multiple unknown tokens deterministically, meaning that a single prediction of a masked model holds additional information unused by standard sampling procedures. Based on this observation, we introduce EB-Sampler, a simple drop-in replacement for existing samplers, utilizing an Entropy Bounded unmasking procedure that dynamically unmasks multiple tokens in one function evaluation with predefined approximate error tolerance. We formulate the EB-Sampler as part of a broad family of adaptive samplers for which we provide an error analysis that motivates our algorithmic choices. EB-Sampler accelerates sampling from current state of the art MDMs by roughly 2-3x on standard coding and math reasoning benchmarks without loss in performance. We also validate the same procedure works well on smaller reasoning tasks including maze navigation and Sudoku, tasks ARMs often struggle with.

