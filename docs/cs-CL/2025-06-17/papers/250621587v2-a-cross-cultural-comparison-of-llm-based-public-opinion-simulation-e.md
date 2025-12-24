---
layout: default
title: "A Cross-Cultural Comparison of LLM-based Public Opinion Simulation: Evaluating Chinese and U.S. Models on Diverse Societies"
---

# A Cross-Cultural Comparison of LLM-based Public Opinion Simulation: Evaluating Chinese and U.S. Models on Diverse Societies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21587" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21587v2</a>
  <a href="https://arxiv.org/pdf/2506.21587.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21587v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21587v2', 'A Cross-Cultural Comparison of LLM-based Public Opinion Simulation: Evaluating Chinese and U.S. Models on Diverse Societies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihong Qi, Fan Huang, Jisun An, Haewoon Kwak

**分类**: cs.CL

**发布日期**: 2025-06-17 (更新: 2025-09-12)

---

## 💡 一句话要点

**评估LLM在中美社会中模拟公众意见的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `公众意见模拟` `中美比较` `文化偏见` `社会问题预测` `开源模型` `数据集分析`

## 📋 核心要点

1. 现有的LLM在模拟不同文化背景下的公众意见时，往往存在过度概括和偏见的问题，无法准确反映多样化的社会观点。
2. 论文提出通过比较不同LLM在中美社会中的表现，探索如何改进公众意见模拟的准确性，特别是针对不同人口特征的模型训练方法。
3. 实验结果显示，DeepSeek-V3在模拟美国堕胎问题的公众意见时表现最佳，但在模拟中国公众对资本主义的看法时存在显著局限性，提示了模型的改进方向。

## 📝 摘要（中文）

本研究评估了开源大型语言模型DeepSeek在模拟公众意见方面的能力，并与主要科技公司开发的LLM进行比较。通过对DeepSeek-R1和DeepSeek-V3与Qwen2.5、GPT-4o和Llama-3.3的比较，以及利用美国国家选举研究（ANES）和中国的Zuobiao数据集，我们评估了这些模型在中美社会问题上的公众意见预测能力。研究发现，DeepSeek-V3在模拟美国关于堕胎问题的意见时表现最佳，但在其他主题上表现有限，尤其是在模拟低收入和非大学教育个体对资本主义的看法时存在不足。这些结果强调了在LLM驱动的公众意见建模中减轻文化和人口偏见的必要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有大型语言模型（LLM）在模拟中美公众意见时的不足，特别是如何准确捕捉不同文化和人口特征的观点。现有方法常常过度概括，无法反映多样化的社会意见。

**核心思路**：论文的核心思路是通过比较开源模型DeepSeek与商业模型在不同社会问题上的表现，评估其在公众意见模拟中的能力，并提出改进建议。设计上强调了对不同人口特征的适应性。

**技术框架**：研究采用了多阶段的比较分析框架，包括数据收集（ANES和Zuobiao数据集）、模型训练（DeepSeek-R1、DeepSeek-V3与其他模型的对比）、以及结果评估（针对不同社会问题的公众意见模拟）。

**关键创新**：最重要的技术创新点在于引入了开源模型DeepSeek，并通过与商业模型的对比，揭示了不同模型在模拟公众意见时的优缺点，特别是在文化和人口特征的适应性方面。

**关键设计**：在模型训练中，采用了针对不同社会问题的特定数据集，设置了多样化的人物角色（如民主党或自由派角色），并关注了模型在不同人口群体中的表现差异。

## 📊 实验亮点

实验结果表明，DeepSeek-V3在模拟美国公众对堕胎问题的意见时表现最佳，相较于其他主题如气候变化、枪支管控等，提升幅度显著。此外，DeepSeek-V3在模拟中国公众对外援和个人主义的看法时表现较好，但在资本主义的模拟上存在明显局限，未能有效捕捉低收入和非大学教育个体的观点。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学研究、政策制定和舆情分析等。通过改进公众意见模拟的准确性，能够更好地理解和预测社会动态，为决策者提供数据支持，促进社会治理的科学化和精准化。

## 📄 摘要（原文）

> This study evaluates the ability of DeepSeek, an open-source large language model (LLM), to simulate public opinions in comparison to LLMs developed by major tech companies. By comparing DeepSeek-R1 and DeepSeek-V3 with Qwen2.5, GPT-4o, and Llama-3.3 and utilizing survey data from the American National Election Studies (ANES) and the Zuobiao dataset of China, we assess these models' capacity to predict public opinions on social issues in both China and the United States, highlighting their comparative capabilities between countries. Our findings indicate that DeepSeek-V3 performs best in simulating U.S. opinions on the abortion issue compared to other topics such as climate change, gun control, immigration, and services for same-sex couples, primarily because it more accurately simulates responses when provided with Democratic or liberal personas. For Chinese samples, DeepSeek-V3 performs best in simulating opinions on foreign aid and individualism but shows limitations in modeling views on capitalism, particularly failing to capture the stances of low-income and non-college-educated individuals. It does not exhibit significant differences from other models in simulating opinions on traditionalism and the free market. Further analysis reveals that all LLMs exhibit the tendency to overgeneralize a single perspective within demographic groups, often defaulting to consistent responses within groups. These findings highlight the need to mitigate cultural and demographic biases in LLM-driven public opinion modeling, calling for approaches such as more inclusive training methodologies.

