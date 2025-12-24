---
layout: default
title: "UrbanSense:A Framework for Quantitative Analysis of Urban Streetscapes leveraging Vision Large Language Models"
---

# UrbanSense:A Framework for Quantitative Analysis of Urban Streetscapes leveraging Vision Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10342" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10342v2</a>
  <a href="https://arxiv.org/pdf/2506.10342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10342v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10342v2', 'UrbanSense:A Framework for Quantitative Analysis of Urban Streetscapes leveraging Vision Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Yin, Jing Zhong, Peilin Li, Ruolin Pan, Pengyu Zeng, Miao Zhang, Shuai Lu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-08-04)

---

## 💡 一句话要点

**提出UrbanSense框架以解决城市街景定量分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市街景` `视觉语言模型` `多模态分析` `数据集构建` `风格比较` `定量分析` `建筑设计` `城市文化`

## 📋 核心要点

1. 现有的城市文化研究方法依赖专家解读和历史文献，缺乏标准化和客观性。
2. 本文提出了一种基于视觉语言模型的多模态框架，能够自动化分析城市街景风格差异。
3. 实验结果显示，生成描述的有效性高，主观评估的Phi分数表明该方法能捕捉细微的风格差异。

## 📝 摘要（中文）

城市文化和建筑风格因地理、历史和社会政治因素而异，理解这些差异对未来城市发展至关重要。本文提出了一种基于视觉语言模型的多模态研究框架，旨在实现城市街景风格差异的自动化和可扩展分析。我们构建了UrbanDiffBench数据集，并开发了UrbanSense框架，能够定量生成和比较城市风格表现。实验结果显示，超过80%的生成描述通过t检验，主观评估的Phi分数也表明该方法能有效捕捉细微的风格差异，提供了科学的城市设计视角。

## 🔬 方法详解

**问题定义**：本文旨在解决传统城市文化研究方法的主观性和标准化不足的问题，现有方法难以实现对城市街景风格的量化分析。

**核心思路**：通过构建基于视觉语言模型的多模态框架，自动化分析城市街景的风格差异，从而提高研究的客观性和数据驱动性。

**技术框架**：该框架包括数据集构建、模型训练和风格分析三个主要模块。首先，构建UrbanDiffBench数据集，包含不同历史时期和地区的建筑图像；其次，利用视觉语言模型进行训练；最后，进行风格生成和比较分析。

**关键创新**：UrbanSense是首个基于视觉语言模型的城市街景分析框架，能够实现风格表现的定量生成与比较，显著提升了分析的客观性。

**关键设计**：在模型设计中，采用了特定的损失函数以优化风格生成效果，并通过多层卷积神经网络提取图像特征，确保生成描述的准确性与丰富性。实验中，参数设置经过调优，以提高模型的性能。

## 📊 实验亮点

实验结果显示，超过80%的生成描述通过t检验（p < 0.05），主观评估的Phi分数为0.912（城市）和0.833（时期），表明该方法在捕捉细微风格差异方面具有显著优势，验证了其有效性。

## 🎯 应用场景

该研究可广泛应用于城市规划、建筑设计和文化遗产保护等领域，帮助设计师和研究者更好地理解和预测城市风格的演变。通过定量分析，能够为未来的城市设计提供科学依据，促进城市文化的可持续发展。

## 📄 摘要（原文）

> Urban cultures and architectural styles vary significantly across cities due to geographical, chronological, historical, and socio-political factors. Understanding these differences is essential for anticipating how cities may evolve in the future. As representative cases of historical continuity and modern innovation in China, Beijing and Shenzhen offer valuable perspectives for exploring the transformation of urban streetscapes. However, conventional approaches to urban cultural studies often rely on expert interpretation and historical documentation, which are difficult to standardize across different contexts. To address this, we propose a multimodal research framework based on vision-language models, enabling automated and scalable analysis of urban streetscape style differences. This approach enhances the objectivity and data-driven nature of urban form research. The contributions of this study are as follows: First, we construct UrbanDiffBench, a curated dataset of urban streetscapes containing architectural images from different periods and regions. Second, we develop UrbanSense, the first vision-language-model-based framework for urban streetscape analysis, enabling the quantitative generation and comparison of urban style representations. Third, experimental results show that Over 80% of generated descriptions pass the t-test (p less than 0.05). High Phi scores (0.912 for cities, 0.833 for periods) from subjective evaluations confirm the method's ability to capture subtle stylistic differences. These results highlight the method's potential to quantify and interpret urban style evolution, offering a scientifically grounded lens for future design.

