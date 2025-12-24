---
layout: default
title: R2R: Efficiently Navigating Divergent Reasoning Paths with Small-Large Model Token Routing
---

# R2R: Efficiently Navigating Divergent Reasoning Paths with Small-Large Model Token Routing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21600" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21600v2</a>
  <a href="https://arxiv.org/pdf/2505.21600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21600v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21600v2', 'R2R: Efficiently Navigating Divergent Reasoning Paths with Small-Large Model Token Routing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyu Fu, Yi Ge, Yichen You, Enshu Liu, Zhihang Yuan, Guohao Dai, Shengen Yan, Huazhong Yang, Yu Wang

**分类**: cs.CL, cs.AI, cs.LG, cs.PF

**发布日期**: 2025-05-27 (更新: 2025-11-05)

**🔗 代码/项目**: [GITHUB](https://github.com/thu-nics/R2R)

---

## 💡 一句话要点

**提出R2R以高效导航语言模型推理路径**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `小型语言模型` `推理效率` `token路由` `自动数据生成` `性能提升` `计算资源优化`

## 📋 核心要点

1. 现有的大型语言模型在推理能力上表现优异，但其高推理开销限制了实际应用。
2. R2R方法通过识别并仅对关键的分歧token使用大型语言模型，从而提高了推理效率。
3. 实验结果显示，R2R在5.6B参数下的准确率比R1-7B高出1.6倍，并且在速度上比R1-32B快2.8倍。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理能力上表现出色，但其推理开销巨大，给部署带来了挑战。尽管蒸馏的小型语言模型（SLMs）显著提高了效率，但由于无法跟随LLMs的推理路径，其性能受到影响。我们发现，只有少量的token真正导致了LLMs与SLMs之间的推理路径分歧。基于这一发现，我们提出了R2R，一种神经token路由方法，仅对这些关键的分歧token使用LLMs，而将大部分token生成留给SLMs。我们还开发了自动数据生成管道，识别分歧token并生成token级路由标签以训练轻量级路由器。R2R在多个基准测试中表现优异，超越了现有模型的性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型（LLMs）在推理时的高开销问题。现有的小型语言模型（SLMs）虽然提高了效率，但在推理路径上无法跟随LLMs，导致性能下降。

**核心思路**：我们发现，LLMs与SLMs之间的推理路径分歧主要集中在少量token上。R2R方法通过选择性地对这些关键token使用LLMs，优化了推理过程，减少了不必要的计算。

**技术框架**：R2R的整体架构包括一个自动数据生成管道，用于识别分歧token并生成相应的路由标签。该框架由轻量级路由器和SLMs组成，路由器负责决定哪些token需要使用LLMs进行处理。

**关键创新**：R2R的核心创新在于其token路由机制，能够有效区分关键的分歧token与其他token，从而在保持性能的同时显著降低推理开销。这一设计与传统方法的根本区别在于其选择性使用LLMs。

**关键设计**：在R2R中，关键参数设置包括路由器的训练数据生成策略和损失函数设计。此外，网络结构上，轻量级路由器与SLMs的结合使得整体模型在推理时更加高效。通过这些设计，R2R实现了在准确率和速度上的双重提升。

## 📊 实验亮点

R2R在多个基准测试中表现出色，平均激活参数大小为5.6B，准确率比R1-7B高出1.6倍，甚至超越了R1-14B模型。同时，相比于R1-32B，R2R在推理速度上实现了2.8倍的提升，显著推进了测试时间的扩展效率。

## 🎯 应用场景

R2R方法具有广泛的应用潜力，尤其在需要高效推理的场景中，如智能问答、编程辅助和复杂数学问题求解等领域。其高效的推理能力可以推动大型语言模型在实际应用中的普及，降低计算资源消耗，提高用户体验。

## 📄 摘要（原文）

> Large Language Models (LLMs) achieve impressive reasoning capabilities at the cost of substantial inference overhead, posing substantial deployment challenges. Although distilled Small Language Models (SLMs) significantly enhance efficiency, their performance suffers as they fail to follow LLMs' reasoning paths. Luckily, we reveal that only a small fraction of tokens genuinely diverge reasoning paths between LLMs and SLMs. Most generated tokens are either identical or exhibit neutral differences, such as minor variations in abbreviations or expressions. Leveraging this insight, we introduce **Roads to Rome (R2R)**, a neural token routing method that selectively utilizes LLMs only for these critical, path-divergent tokens, while leaving the majority of token generation to the SLM. We also develop an automatic data generation pipeline that identifies divergent tokens and generates token-level routing labels to train the lightweight router. We apply R2R to combine R1-1.5B and R1-32B models from the DeepSeek family, and evaluate on challenging math, coding, and QA benchmarks. With an average activated parameter size of 5.6B, R2R surpasses the average accuracy of R1-7B by 1.6x, outperforming even the R1-14B model. Compared to R1-32B, it delivers a 2.8x wall-clock speedup with comparable performance, advancing the Pareto frontier of test-time scaling efficiency. Our code is available at https://github.com/thu-nics/R2R.

