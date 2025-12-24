---
layout: default
title: Cache-Efficient Posterior Sampling for Reinforcement Learning with LLM-Derived Priors Across Discrete and Continuous Domains
---

# Cache-Efficient Posterior Sampling for Reinforcement Learning with LLM-Derived Priors Across Discrete and Continuous Domains

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07274" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07274v1</a>
  <a href="https://arxiv.org/pdf/2505.07274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07274v1', 'Cache-Efficient Posterior Sampling for Reinforcement Learning with LLM-Derived Priors Across Discrete and Continuous Domains')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma

**分类**: cs.LG

**发布日期**: 2025-05-12

**期刊**: Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing

---

## 💡 一句话要点

**提出缓存高效的后验采样框架以降低RL计算成本**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

## 📋 核心要点

1. 现有方法在将大型语言模型应用于强化学习时面临高计算成本和延迟问题，限制了其实际应用。
2. 本文提出了一种自适应缓存机制，通过元优化缓存参数，显著提高了后验采样的效率，适用于离散和连续控制领域。
3. 实验表明，该框架在多个任务中实现了3.8-4.7倍的LLM查询减少和4.0-12.0倍的延迟降低，同时保持了96-98%的性能。
4. method_zh”: “**问题定义**：本文旨在解决将大型语言模型作为先验信息时的高计算成本和延迟问题。现有方法在处理复杂环境时，往往需要频繁调用LLM，导致效率低下。\n\n**核心思路**：提出了一种基于自适应缓存的后验采样框架，通过元优化缓存参数，利用代理梯度来提升性能，从而降低LLM的查询频率和延迟。\n\n**技术框架**：整体架构包括自适应缓存机制、后验采样模块和性能评估模块。自适应缓存机制根据策略性能动态调整缓存参数，确保高效推理。\n\n**关键创新**：最重要的创新在于自适应缓存机制的设计，使得在保持高性能的同时，显著减少了对LLM的查询需求。这一设计与传统方法的静态缓存策略形成鲜明对比。\n\n**关键设计**：关键参数设置包括缓存大小、更新频率等，损失函数采用了基于KL散度的近似质量评估，确保了在不同环境下的有效性和稳定性。
5. application_zh”: “该研究的潜在应用领域包括自然语言处理、机器人控制和游戏AI等。通过降低计算成本，该框架能够在资源受限的环境中实现高效的强化学习，推动智能系统的实际应用和发展。”
6. highlight_zh”: “实验结果显示，提出的框架在多个任务中实现了3.8-4.7倍的LLM查询减少和4.0-12.0倍的延迟降低，同时保持了96-98%的性能。此外，在离线RL中，CQL-Prior变体提升了14-29%的性能，并减少了38-40%的训练时间。”
7. tags_zh”: [
8. 缓存机制
9. 后验采样
10. 强化学习
11. 大型语言模型
12. 自适应优化
13. 离线强化学习
14. 性能提升

## 📝 摘要（中文）

将大型语言模型（LLMs）作为强化学习（RL）的先验信息，虽然能带来显著优势，但也伴随高昂的计算成本。本文提出了一种原则性的缓存高效框架，通过自适应缓存机制，显著降低了LLM查询次数和延迟，同时保持高性能。该方法在离线RL中也表现出色，提升了14-29%的性能，并减少了38-40%的训练时间。实验结果表明，该框架在资源受限的环境中具有良好的通用性和实用性。

## 📄 摘要（原文）

> Integrating large language models (LLMs) as priors in reinforcement learning (RL) offers significant advantages but comes with substantial computational costs. We present a principled cache-efficient framework for posterior sampling with LLM-derived priors that dramatically reduces these costs while maintaining high performance. At the core of our approach is an adaptive caching mechanism, where cache parameters are meta-optimized using surrogate gradients derived from policy performance. This design enables efficient inference across both discrete text environments (e.g., TextWorld, ALFWorld) and continuous control domains (e.g., MuJoCo), achieving a 3.8--4.7$\times$ reduction in LLM queries and 4.0--12.0$\times$ lower median latencies (85--93\,ms on a consumer GPU) while retaining 96--98\% of uncached performance. Our theoretical analysis provides KL divergence bounds on approximation quality, validated empirically. The framework extends to offline RL, where our CQL-Prior variant improves performance by 14--29\% and reduces training time by 38--40\%. Extensive evaluations across a diverse suite of eight tasks demonstrate the generalizability and practical viability of LLM-guided RL in resource-constrained settings.

