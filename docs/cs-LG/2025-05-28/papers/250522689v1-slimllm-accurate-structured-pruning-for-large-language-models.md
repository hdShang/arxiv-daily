---
layout: default
title: SlimLLM: Accurate Structured Pruning for Large Language Models
---

# SlimLLM: Accurate Structured Pruning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.22689" class="toolbar-btn" target="_blank">📄 arXiv: 2505.22689v1</a>
  <a href="https://arxiv.org/pdf/2505.22689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.22689v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.22689v1', 'SlimLLM: Accurate Structured Pruning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang

**分类**: cs.LG

**发布日期**: 2025-05-28

**备注**: ICML 2025

---

## 💡 一句话要点

**提出SlimLLM以解决大语言模型的结构化剪枝问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `结构化剪枝` `模型压缩` `性能恢复` `通道重要性评估` `注意力头剪枝` `线性回归策略`

## 📋 核心要点

1. 现有的结构化剪枝方法在评估子模块重要性时，往往只关注单个元素，未能充分考虑元素间的相互依赖性。
2. SlimLLM通过整体评估通道和注意力头的重要性，提出了一种新的剪枝策略，并引入线性回归以快速恢复模型性能。
3. 在LLaMA基准测试中，SlimLLM的表现优于其他剪枝方法，展示了其在大语言模型压缩中的有效性。

## 📝 摘要（中文）

大语言模型（LLMs）因其巨大的计算成本而限制了其部署和应用。为了解决这一问题，结构化剪枝成为压缩LLMs参数的有效方案。本文提出了一种名为SlimLLM的快速结构化剪枝方法，通过评估整个通道或注意力头的重要性，考虑了子模块内元素之间的相互依赖。此外，设计了简单的线性回归策略以快速恢复性能，并提出基于层的重要性比率来确定每层的剪枝比例。基于LLaMA基准测试结果，SlimLLM在性能上超越了其他方法，达到了最先进的水平。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型的结构化剪枝问题，现有方法在评估子模块重要性时存在局限，未能考虑元素间的相互依赖性，导致性能损失。

**核心思路**：SlimLLM通过整体评估通道和注意力头的重要性，避免了仅依赖单个元素的重要性聚合，从而实现更有效的剪枝。同时，设计了线性回归策略以快速恢复模型性能。

**技术框架**：SlimLLM的整体架构包括重要性评估模块、剪枝决策模块和性能恢复模块。重要性评估模块负责计算通道和注意力头的重要性，剪枝决策模块根据层的重要性比率确定剪枝比例，性能恢复模块则通过线性回归快速恢复模型性能。

**关键创新**：SlimLLM的主要创新在于其整体重要性评估方法，考虑了子模块内元素的相互依赖性，显著提高了剪枝的有效性和模型的保留性能。

**关键设计**：在参数设置上，SlimLLM采用了基于层的重要性比率来动态调整每层的剪枝比例，损失函数设计上则结合了线性回归以优化输出矩阵的恢复效果。整体网络结构保持了大语言模型的基本架构，确保了剪枝后的模型仍具备良好的性能。

## 📊 实验亮点

在LLaMA基准测试中，SlimLLM的性能超越了现有的剪枝方法，达到了最先进的水平，具体提升幅度未知。该方法在剪枝效率和模型性能恢复方面表现出色，展示了其在大语言模型压缩领域的显著优势。

## 🎯 应用场景

SlimLLM的研究成果在大语言模型的实际应用中具有广泛的潜力，尤其是在资源受限的环境中，如移动设备和边缘计算。通过有效的结构化剪枝，SlimLLM能够在保证模型性能的前提下，显著降低计算和存储成本，推动大语言模型在实际应用中的普及和推广。

## 📄 摘要（原文）

> Large language models(LLMs) have garnered significant attention and demonstrated impressive capabilities in a wide range of applications. However, due to their enormous computational costs, the deployment and application of LLMs are often severely limited. To address this issue, structured pruning is an effective solution to compress the parameters of LLMs. Determining the importance of each sub-module in LLMs and minimizing performance loss are critical issues that need to be carefully addressed in structured pruning. In this paper, we propose an effective and fast structured pruning method named SlimLLM for large language models. For channel and attention head pruning, we evaluate the importance based on the entire channel or head, rather than merely aggregating the importance of individual elements within a sub-module. This approach enables a more holistic consideration of the interdependence among elements within the sub-module. In addition, we design a simple linear regression strategy for the output matrix to quickly recover performance. We also propose layer-based importance ratio to determine the pruning ratio for each layer. Based on the LLaMA benchmark results, our SlimLLM outperforms other methods and achieves state-of-the-art performance.

