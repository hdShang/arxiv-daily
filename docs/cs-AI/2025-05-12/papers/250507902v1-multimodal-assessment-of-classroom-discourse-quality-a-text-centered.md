---
layout: default
title: Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach
---

# Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07902" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07902v1</a>
  <a href="https://arxiv.org/pdf/2505.07902.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07902v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07902v1', 'Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, Enkelejda Kasneci

**分类**: cs.CY, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-12

**备注**: The 18th International Conference on Educational Data Mining (EDM 2025)

---

## 💡 一句话要点

**提出多模态融合架构以评估课堂话语质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `课堂话语评估` `多模态融合` `注意力机制` `多任务学习` `序数分类` `教育技术` `自动化评估`

## 📋 核心要点

1. 现有方法主要依赖手动编码，耗时且难以扩展，无法有效评估整个课堂段落的教学质量。
2. 本研究提出了一种多模态融合架构，利用注意力机制和多任务学习，联合评估课堂话语的多个维度。
3. 实验结果显示，模型在GTI德国数据集上取得了0.384的Kappa评分，接近人类评分一致性，验证了方法的有效性。

## 📝 摘要（中文）

课堂话语是教学与学习的重要载体，评估话语实践的不同特征并将其与学生学习成就关联，有助于理解教学质量。传统评估依赖于手动编码课堂观察协议，耗时且成本高。尽管已有研究利用AI技术分析课堂话语，但对整个课程段落的评估仍然有限。为此，本研究提出了一种新颖的文本中心多模态融合架构，评估基于全球教学洞察（GTI）观察协议的三种话语成分的质量。通过注意力机制捕捉文本、音频和视频流的交互，采用多任务学习方法联合预测三种成分的质量评分，并将任务形式化为序数分类问题。实验结果表明，文本模态在任务中占主导地位，整合声学特征提高了模型与人类评分的一致性。

## 🔬 方法详解

**问题定义**：本研究旨在解决课堂话语质量评估的不足，尤其是现有方法在处理整个课程段落时的局限性，传统方法耗时且难以实现自动化。

**核心思路**：提出了一种文本中心的多模态融合架构，通过注意力机制捕捉不同模态间的交互，采用多任务学习方法联合预测话语质量评分，以提高评估的准确性和效率。

**技术框架**：整体架构包括三个主要模块：文本、音频和视频流的输入，注意力机制用于捕捉模态间的交互，最后通过多任务学习模型输出三种话语成分的质量评分。

**关键创新**：本研究的创新在于将多模态数据融合与多任务学习相结合，特别是将任务形式化为序数分类问题，以更好地反映评分的等级顺序，这在现有研究中尚属首次。

**关键设计**：在模型设计中，采用了适应性损失函数以优化多任务学习的效果，注意力机制的参数设置经过调优，以确保不同模态的有效融合，网络结构则基于深度学习框架进行构建，确保高效的特征提取和融合。

## 📊 实验亮点

实验结果表明，整合声学特征后，模型与人类评分的一致性显著提高，Kappa评分达到0.384，接近人类评分的一致性（0.326），展示了多模态融合在课堂话语质量评估中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、教师专业发展和课堂教学质量监测。通过自动化的课堂话语质量评估，教师可以获得及时反馈，从而改进教学策略，提升学生学习效果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Classroom discourse is an essential vehicle through which teaching and learning take place. Assessing different characteristics of discursive practices and linking them to student learning achievement enhances the understanding of teaching quality. Traditional assessments rely on manual coding of classroom observation protocols, which is time-consuming and costly. Despite many studies utilizing AI techniques to analyze classroom discourse at the utterance level, investigations into the evaluation of discursive practices throughout an entire lesson segment remain limited. To address this gap, our study proposes a novel text-centered multimodal fusion architecture to assess the quality of three discourse components grounded in the Global Teaching InSights (GTI) observation protocol: Nature of Discourse, Questioning, and Explanations. First, we employ attention mechanisms to capture inter- and intra-modal interactions from transcript, audio, and video streams. Second, a multi-task learning approach is adopted to jointly predict the quality scores of the three components. Third, we formulate the task as an ordinal classification problem to account for rating level order. The effectiveness of these designed elements is demonstrated through an ablation study on the GTI Germany dataset containing 92 videotaped math lessons. Our results highlight the dominant role of text modality in approaching this task. Integrating acoustic features enhances the model's consistency with human ratings, achieving an overall Quadratic Weighted Kappa score of 0.384, comparable to human inter-rater reliability (0.326). Our study lays the groundwork for the future development of automated discourse quality assessment to support teacher professional development through timely feedback on multidimensional discourse practices.

