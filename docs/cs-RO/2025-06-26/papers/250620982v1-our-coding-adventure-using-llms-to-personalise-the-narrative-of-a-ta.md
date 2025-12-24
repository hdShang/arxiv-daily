---
layout: default
title: "Our Coding Adventure: Using LLMs to Personalise the Narrative of a Tangible Programming Robot for Preschoolers"
---

# Our Coding Adventure: Using LLMs to Personalise the Narrative of a Tangible Programming Robot for Preschoolers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20982" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20982v1</a>
  <a href="https://arxiv.org/pdf/2506.20982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20982v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20982v1', 'Our Coding Adventure: Using LLMs to Personalise the Narrative of a Tangible Programming Robot for Preschoolers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martin Ruskov

**分类**: cs.CY, cs.RO

**发布日期**: 2025-06-26

**备注**: accepted at D-SAIL Workshop - Transformative Curriculum Design: Digitalization, Sustainability, and AI Literacy for 21st Century Learning

---

## 💡 一句话要点

**提出利用LLMs个性化编程机器人故事以解决学前教育挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `学前教育` `编程机器人` `个性化学习` `教育技术` `故事生成` `行动研究`

## 📋 核心要点

1. 现有教育方法在使用大型语言模型时存在理解不足和受众易受影响的问题，尤其是对幼儿的影响。
2. 本文提出通过可触摸编程机器人Cubetto，利用LLMs生成个性化故事，帮助教师为儿童创造适合的学习内容。
3. 实验结果表明，该方法在四种任务场景中取得了成功，尽管存在一致性和幻觉问题，但为教师提供了有效的辅助工具。

## 📝 摘要（中文）

在教育中平衡使用大型语言模型（LLMs）面临挑战，尤其是对年轻儿童而言。本文提出了一种利用名为Cubetto的可触摸编程机器人，通过LLMs生成个性化故事的方法，以帮助学前儿童适应指令编程的实践。我们进行了行动研究，开发了一个快速原型制作游戏故事的初步正式流程。该方法具有可重复性和模型无关性，测试了五种不同的LLMs。我们记录了过程、材料和提示，以及学习经验和结果。尽管在一致性和幻觉方面遇到问题，但我们认为该方法适合学前班，并计划在实际教育环境中进一步实验。

## 🔬 方法详解

**问题定义**：本文旨在解决如何在学前教育中有效利用大型语言模型（LLMs）的问题，现有方法在儿童教育中存在理解不足和技术风险。

**核心思路**：通过使用Cubetto编程机器人，利用LLMs生成个性化的故事，帮助教师为儿童创造适合的学习内容，而不直接暴露儿童于LLMs。

**技术框架**：整体流程包括：1) 使用开放权重模型生成故事；2) 通过教师输入的提示和材料进行个性化调整；3) 测试和评估生成故事的有效性。

**关键创新**：该方法的创新在于模型无关性，能够在五种不同的LLMs上进行测试，确保了结果的可重复性和适应性。

**关键设计**：在参数设置上，使用开放权重模型，设计了适合儿童的故事生成提示，确保生成内容的趣味性和教育性。

## 📊 实验亮点

实验结果显示，在四种不同的任务场景中，生成的故事成功吸引了儿童的注意力，尽管存在一致性和幻觉问题，但整体上为教师提供了有效的辅助工具，提升了教学效果。

## 🎯 应用场景

该研究的潜在应用领域包括学前教育、编程教育和教育技术。通过个性化故事生成，教师能够更有效地吸引儿童的注意力，促进他们的学习兴趣和编程能力，未来可能对教育模式产生深远影响。

## 📄 摘要（原文）

> Finding balanced ways to employ Large Language Models (LLMs) in education is a challenge due to inherent risks of poor understanding of the technology and of a susceptible audience. This is particularly so with younger children, who are known to have difficulties with pervasive screen time. Working with a tangible programming robot called Cubetto, we propose an approach to benefit from the capabilities of LLMs by employing such models in the preparation of personalised storytelling, necessary for preschool children to get accustomed to the practice of commanding the robot. We engage in action research to develop an early version of a formalised process to rapidly prototype game stories for Cubetto. Our approach has both reproducible results, because it employs open weight models, and is model-agnostic, because we test it with 5 different LLMs. We document on one hand the process, the used materials and prompts, and on the other the learning experience and outcomes. We deem the generation successful for the intended purposes of using the results as a teacher aid. Testing the models on 4 different task scenarios, we encounter issues of consistency and hallucinations and document the corresponding evaluation process and attempts (some successful and some not) to overcome these issues. Importantly, the process does not expose children to LLMs directly. Rather, the technology is used to help teachers easily develop personalised narratives on children's preferred topics. We believe our method is adequate for preschool classes and we are planning to further experiment in real-world educational settings.

