---
layout: default
title: "HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America"
---

# HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24712" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24712v1</a>
  <a href="https://arxiv.org/pdf/2505.24712.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24712v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24712v1', 'HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings in Latin America')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guido Ivetta, Marcos J. Gomez, Sofía Martinelli, Pietro Palombini, M. Emilia Echeveste, Nair Carolina Mazzeo, Beatriz Busaniche, Luciana Benotti

**分类**: cs.CL, cs.CY

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出HESEIA数据集以评估语言模型中的社会偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社会偏见` `语言模型` `数据集` `教育研究` `交叉偏见` `参与式设计` `拉丁美洲`

## 📋 核心要点

1. 现有评估大型语言模型社会偏见的方法缺乏社区参与，导致数据集的代表性不足。
2. HESEIA数据集通过教师和学生的共同设计，捕捉了多种人口统计特征下的交叉偏见，反映了地方教育背景。
3. 实验结果表明，HESEIA数据集包含更多当前大型语言模型未识别的刻板印象，提升了偏见评估的有效性。

## 📝 摘要（中文）

大多数用于评估大型语言模型中社会偏见的资源缺乏来自受影响社区的共同设计，且很少采用参与式方法。我们介绍了HESEIA，一个由46,499个句子组成的数据集，创建于一个专业发展课程中。该课程涉及370名高中教师和5,370名来自189所拉丁美洲学校的学生。与现有基准不同，HESEIA捕捉了跨多个人口统计轴和学科的交叉偏见，反映了教育者的生活经验和教学专业知识。教师们使用最小对比对创建表达与其学科和社区相关的刻板印象的句子。我们展示了数据集在代表的人口统计轴和知识领域方面的多样性，并证明该数据集包含比以往数据集更多当前大型语言模型未识别的刻板印象。HESEIA可用于支持基于教育社区的偏见评估。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大型语言模型评估中缺乏社区参与和代表性的问题。现有方法往往忽视了受影响群体的声音，导致偏见评估不全面。

**核心思路**：HESEIA数据集的核心思路是通过教师和学生的共同参与，创建一个反映地方文化和教育背景的句子集合，从而更全面地捕捉社会偏见。

**技术框架**：该研究的整体架构包括教师培训、句子创作和数据集构建三个主要阶段。教师在专业发展课程中使用最小对比对的方法生成句子，确保句子与其学科和社区相关。

**关键创新**：HESEIA的最大创新在于其参与式设计，确保数据集反映真实的地方偏见和教育背景。这与传统数据集的静态构建方式形成鲜明对比。

**关键设计**：在数据集构建过程中，教师们使用最小对比对生成句子，确保句子表达的刻板印象与教育内容相关，且覆盖多种人口统计特征和知识领域。

## 📊 实验亮点

实验结果显示，HESEIA数据集包含的刻板印象数量显著高于以往数据集，尤其是在未被当前大型语言模型识别的偏见方面。这一发现强调了HESEIA在偏见评估中的重要性，提供了更为丰富的评估基础。

## 🎯 应用场景

HESEIA数据集的潜在应用领域包括教育研究、社会偏见评估和大型语言模型的训练与优化。通过提供一个更具代表性和多样性的数据集，研究人员和开发者可以更好地理解和减轻语言模型中的社会偏见，从而提升其在教育和社会应用中的公平性和有效性。

## 📄 摘要（原文）

> Most resources for evaluating social biases in Large Language Models are developed without co-design from the communities affected by these biases, and rarely involve participatory approaches. We introduce HESEIA, a dataset of 46,499 sentences created in a professional development course. The course involved 370 high-school teachers and 5,370 students from 189 Latin-American schools. Unlike existing benchmarks, HESEIA captures intersectional biases across multiple demographic axes and school subjects. It reflects local contexts through the lived experience and pedagogical expertise of educators. Teachers used minimal pairs to create sentences that express stereotypes relevant to their school subjects and communities. We show the dataset diversity in term of demographic axes represented and also in terms of the knowledge areas included. We demonstrate that the dataset contains more stereotypes unrecognized by current LLMs than previous datasets. HESEIA is available to support bias assessments grounded in educational communities.

