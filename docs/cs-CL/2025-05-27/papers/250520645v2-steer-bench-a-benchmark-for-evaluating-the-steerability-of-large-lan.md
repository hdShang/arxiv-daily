---
layout: default
title: "STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models"
---

# STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20645" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20645v2</a>
  <a href="https://arxiv.org/pdf/2505.20645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20645v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20645v2', 'STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Chen, Zihao He, Taiwei Shi, Kristina Lerman

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-06-04)

---

## 💡 一句话要点

**提出STEER-BENCH以评估大型语言模型的可引导性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可引导性` `社区规范` `评估基准` `Reddit社区` `多样化视角` `人工智能`

## 📋 核心要点

1. 现有方法在评估大型语言模型的可引导性方面存在不足，尤其是在适应不同社区规范和观点时的能力未得到充分验证。
2. 论文提出了Steer-Bench基准，通过对比不同Reddit社区，系统评估LLMs在理解社区特定指令和应对对抗性引导方面的能力。
3. 实验结果显示，尽管人类专家的准确率达到81%，但最佳模型的准确率仅为65%，表明LLMs在社区敏感性方面仍有显著提升空间。

## 📝 摘要（中文）

可引导性，即大型语言模型（LLMs）根据不同社区特定规范、观点和交流风格调整输出的能力，对于实际应用至关重要，但仍未得到充分评估。我们介绍了Steer-Bench，这是一个用于评估人口特定引导的基准，涵盖了30对对比的Reddit子社区，涉及19个领域，包含超过10,000个指令-响应对和验证的5,500个多项选择题及其对应的银标签，以测试与多样化社区规范的一致性。对13个流行LLMs的评估显示，尽管人类专家在银标签上的准确率为81%，但表现最佳的模型在不同领域和配置下的准确率仅约为65%。一些模型在社区敏感的可引导性方面落后于人类水平超过15个百分点，突显了显著的差距。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在适应不同社区规范和观点时的可引导性评估不足的问题。现有方法未能有效捕捉模型在社区特定指令下的表现和对抗性引导的抵抗能力。

**核心思路**：论文的核心思路是通过构建Steer-Bench基准，利用对比的Reddit社区来评估LLMs的可引导性，确保模型能够准确理解和响应社区特定的交流风格和规范。

**技术框架**：Steer-Bench的整体架构包括30对对比的子社区，涵盖19个领域，提供超过10,000个指令-响应对和5,500个经过验证的多项选择题，形成一个系统化的评估流程。

**关键创新**：最重要的技术创新点在于引入了社区特定的评估标准，系统性地量化了LLMs在不同社区背景下的表现，填补了现有评估方法的空白。

**关键设计**：在设计中，采用了银标签作为评估标准，并通过多项选择题的形式验证模型的输出，确保评估的准确性和可靠性。

## 📊 实验亮点

实验结果显示，尽管人类专家在使用银标签时的准确率达到81%，但最佳表现的模型在不同领域和配置下的准确率仅为65%。一些模型在社区敏感性方面的表现落后于人类水平超过15个百分点，揭示了当前LLMs在可引导性方面的显著不足。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、在线社区管理和个性化推荐系统等。通过提高大型语言模型的可引导性，可以更好地满足不同用户群体的需求，提升用户体验和满意度。未来，Steer-Bench可能成为评估和优化语言模型在多样化文化和意识形态背景下表现的重要工具。

## 📄 摘要（原文）

> Steerability, or the ability of large language models (LLMs) to adapt outputs to align with diverse community-specific norms, perspectives, and communication styles, is critical for real-world applications but remains under-evaluated. We introduce Steer-Bench, a benchmark for assessing population-specific steering using contrasting Reddit communities. Covering 30 contrasting subreddit pairs across 19 domains, Steer-Bench includes over 10,000 instruction-response pairs and validated 5,500 multiple-choice question with corresponding silver labels to test alignment with diverse community norms. Our evaluation of 13 popular LLMs using Steer-Bench reveals that while human experts achieve an accuracy of 81% with silver labels, the best-performing models reach only around 65% accuracy depending on the domain and configuration. Some models lag behind human-level alignment by over 15 percentage points, highlighting significant gaps in community-sensitive steerability. Steer-Bench is a benchmark to systematically assess how effectively LLMs understand community-specific instructions, their resilience to adversarial steering attempts, and their ability to accurately represent diverse cultural and ideological perspectives.

