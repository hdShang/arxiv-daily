---
layout: default
title: "SAC: A Framework for Measuring and Inducing Personality Traits in LLMs with Dynamic Intensity Control"
---

# SAC: A Framework for Measuring and Inducing Personality Traits in LLMs with Dynamic Intensity Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20993" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20993v1</a>
  <a href="https://arxiv.org/pdf/2506.20993.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20993v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20993v1', 'SAC: A Framework for Measuring and Inducing Personality Traits in LLMs with Dynamic Intensity Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adithya Chittem, Aishna Shrivastava, Sai Tarun Pendela, Jagat Sesh Challa, Dhruv Kumar

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-06-26

**备注**: Under review

---

## 💡 一句话要点

**提出SAC框架以动态控制LLM个性特征的强度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `个性建模` `动态控制` `心理学` `机器学习` `人机交互` `个性特征` `16种个性因素`

## 📋 核心要点

1. 现有的个性建模方法主要依赖大五人格模型，存在个性维度粗糙和缺乏强度控制的不足。
2. 本文提出了特定属性控制（SAC）框架，结合16种个性因素模型，实现对个性特征强度的动态控制。
3. 实验结果显示，连续光谱建模个性强度能显著提高个性表达的可控性，并影响相关特征的心理一致性变化。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在多个领域获得了显著关注，用户期望它们在交互中展现人类般的个性。现有方法主要依赖于大五人格模型，存在个性维度粗糙和缺乏强度控制机制的局限。本文通过扩展机器个性清单（MPI），结合16种个性因素模型，提出了一种名为特定属性控制（SAC）的框架，能够动态评估和诱导LLM的个性特征强度。实验表明，采用连续光谱建模个性强度相比于二元切换，能显著提高个性表达的一致性和可控性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型个性建模中对个性维度粗糙和缺乏强度控制的痛点。现有方法主要依赖大五人格模型，无法细致表达个性特征的变化。

**核心思路**：通过扩展机器个性清单（MPI），结合16种个性因素模型，提出特定属性控制（SAC）框架，以实现对个性特征强度的动态控制，增强个性表达的灵活性和细腻度。

**技术框架**：SAC框架包括多个模块，首先通过形容词语义锚定引导个性特征强度的表达，其次利用五个强度因素（频率、深度、阈值、努力和意愿）进行动态评估和诱导。

**关键创新**：本文的主要创新在于引入了16种个性因素模型，允许对个性特征进行更细致的控制，并通过连续光谱建模提高个性表达的一致性，区别于传统的二元切换方法。

**关键设计**：在模型设计中，采用了基于形容词的语义锚定方法，设置了五个强度因素的评估机制，确保个性特征的表达能够在多维度上进行系统性调整。具体的参数设置和损失函数设计在实验中进行了优化，以提升模型的表现。

## 📊 实验亮点

实验结果表明，采用连续光谱建模个性强度的方式，相比于传统的二元切换方法，个性表达的一致性和可控性显著提高。具体而言，个性特征的动态调整能够系统性地影响相关特征，展现出心理学上的一致性，进一步验证了模型的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、教育和面试等场景，能够实现更为自然和人性化的机器交互。通过动态控制个性特征，LLMs可以更好地适应用户需求，提升用户体验，推动人机交互的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) have gained significant traction across a wide range of fields in recent years. There is also a growing expectation for them to display human-like personalities during interactions. To meet this expectation, numerous studies have proposed methods for modelling LLM personalities through psychometric evaluations. However, most existing models face two major limitations: they rely on the Big Five (OCEAN) framework, which only provides coarse personality dimensions, and they lack mechanisms for controlling trait intensity. In this paper, we address this gap by extending the Machine Personality Inventory (MPI), which originally used the Big Five model, to incorporate the 16 Personality Factor (16PF) model, allowing expressive control over sixteen distinct traits. We also developed a structured framework known as Specific Attribute Control (SAC) for evaluating and dynamically inducing trait intensity in LLMs. Our method introduces adjective-based semantic anchoring to guide trait intensity expression and leverages behavioural questions across five intensity factors: \textit{Frequency}, \textit{Depth}, \textit{Threshold}, \textit{Effort}, and \textit{Willingness}. Through experimentation, we find that modelling intensity as a continuous spectrum yields substantially more consistent and controllable personality expression compared to binary trait toggling. Moreover, we observe that changes in target trait intensity systematically influence closely related traits in psychologically coherent directions, suggesting that LLMs internalize multi-dimensional personality structures rather than treating traits in isolation. Our work opens new pathways for controlled and nuanced human-machine interactions in domains such as healthcare, education, and interviewing processes, bringing us one step closer to truly human-like social machines.

