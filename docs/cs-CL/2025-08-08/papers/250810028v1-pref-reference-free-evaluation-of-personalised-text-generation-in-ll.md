---
layout: default
title: "PREF: Reference-Free Evaluation of Personalised Text Generation in LLMs"
---

# PREF: Reference-Free Evaluation of Personalised Text Generation in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10028" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10028v1</a>
  <a href="https://arxiv.org/pdf/2508.10028.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10028v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10028v1', 'PREF: Reference-Free Evaluation of Personalised Text Generation in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Fu, Hossein A. Rahmani, Bin Wu, Jerome Ramos, Emine Yilmaz, Aldo Lipani

**分类**: cs.CL, cs.AI, cs.HC, cs.LG

**发布日期**: 2025-08-08

**备注**: 7 pages

---

## 💡 一句话要点

**提出PREF框架以解决个性化文本生成评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化文本生成` `评估框架` `无参考评估` `用户偏好` `大型语言模型` `信息系统` `机器学习`

## 📋 核心要点

1. 现有的个性化文本生成评估方法往往忽视用户的个体差异，导致评估结果不够准确和可靠。
2. PREF框架通过无参考的方式，结合用户特定的偏好和上下文，提供了一种新的个性化评估方法。
3. 在PrefEval基准测试中，PREF在准确性和与人类判断的一致性上显著优于现有的强基线方法。

## 📝 摘要（中文）

个性化文本生成对于以用户为中心的信息系统至关重要，但大多数评估方法忽视了用户的个体差异。本文提出了PREF框架，这是一种无参考的个性化评估方法，能够在不需要金标准个性化参考的情况下，综合测量输出质量和用户特定的对齐度。PREF通过三个步骤进行评估：首先，利用大型语言模型生成覆盖普遍标准的查询特定指南；其次，根据目标用户的偏好和上下文对这些标准进行重新排序和选择性增强；最后，使用LLM评估者根据个性化评估标准对候选答案进行评分。实验结果表明，PREF在准确性、校准性和与人类判断的一致性方面优于强基线。

## 🔬 方法详解

**问题定义**：个性化文本生成评估面临的主要问题是现有方法无法考虑用户个体差异，导致评估结果缺乏针对性和准确性。

**核心思路**：PREF框架的核心思想是通过无参考的方式，结合用户的偏好和上下文信息，提供一个个性化的评估标准，从而提高评估的准确性和可靠性。

**技术框架**：PREF的整体架构分为三个主要阶段：覆盖阶段、偏好阶段和评分阶段。覆盖阶段生成通用标准，偏好阶段根据用户特征调整标准，评分阶段使用LLM对候选答案进行评分。

**关键创新**：PREF的创新在于将覆盖与偏好分离，使得评估过程更加透明和可重用，同时允许较小的模型在个性化质量上接近较大的模型。

**关键设计**：在设计中，PREF使用了大型语言模型生成评估标准，并通过用户的显性或隐性偏好对这些标准进行调整，确保评估的个性化和准确性。具体的参数设置和损失函数设计尚未详细说明。

## 📊 实验亮点

在PrefEval基准测试中，PREF的准确性和校准性显著提高，且与人类判断的对齐度更高，具体表现为在隐性偏好跟随任务中，PREF的性能优于多个强基线，展示了其在个性化评估中的有效性。

## 🎯 应用场景

PREF框架在个性化文本生成系统的评估中具有广泛的应用潜力，能够为用户提供更符合其需求的内容生成评估。这一方法的可扩展性和可解释性使其在信息检索、推荐系统等领域具有重要的实际价值，未来可能推动个性化生成技术的进一步发展。

## 📄 摘要（原文）

> Personalised text generation is essential for user-centric information systems, yet most evaluation methods overlook the individuality of users. We introduce \textbf{PREF}, a \textbf{P}ersonalised \textbf{R}eference-free \textbf{E}valuation \textbf{F}ramework that jointly measures general output quality and user-specific alignment without requiring gold personalised references. PREF operates in a three-step pipeline: (1) a coverage stage uses a large language model (LLM) to generate a comprehensive, query-specific guideline covering universal criteria such as factuality, coherence, and completeness; (2) a preference stage re-ranks and selectively augments these factors using the target user's profile, stated or inferred preferences, and context, producing a personalised evaluation rubric; and (3) a scoring stage applies an LLM judge to rate candidate answers against this rubric, ensuring baseline adequacy while capturing subjective priorities. This separation of coverage from preference improves robustness, transparency, and reusability, and allows smaller models to approximate the personalised quality of larger ones. Experiments on the PrefEval benchmark, including implicit preference-following tasks, show that PREF achieves higher accuracy, better calibration, and closer alignment with human judgments than strong baselines. By enabling scalable, interpretable, and user-aligned evaluation, PREF lays the groundwork for more reliable assessment and development of personalised language generation systems.

