---
layout: default
title: A suite of LMs comprehend puzzle statements as well as humans
---

# A suite of LMs comprehend puzzle statements as well as humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08996" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08996v1</a>
  <a href="https://arxiv.org/pdf/2505.08996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08996v1', 'A suite of LMs comprehend puzzle statements as well as humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adele E Goldberg, Supantho Rakshit, Jennifer Hu, Kyle Mahowald

**分类**: cs.CL

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**重新评估大型语言模型在理解英语语句中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `语言理解` `实验设计` `人类与模型比较` `语用敏感性`

## 📋 核心要点

1. 现有研究表明大型语言模型在理解简单英语语句方面的表现被低估，且人类表现被高估。
2. 本文通过对人类在不同条件下的反应进行比较，提出了更自然的理解测试方法，重新评估了LM的能力。
3. 实验结果显示，GPT-4和GPT-o1模型在理解能力上超越了人类，尤其在限制重读的情况下，准确率显著提高。

## 📝 摘要（中文）

近期研究表明，大型语言模型（LMs）在理解简单英语语句方面表现不如人类（Dentella等，2024）。本文重新审视这些发现，认为人类表现被高估，而LM能力被低估。通过对人类在两种条件下的反应进行比较，发现当限制重读时，人类的准确率显著下降（73%），低于Falcon-180B-Chat（76%）和GPT-4（81%）。最新的GPT-o1模型实现了完美准确率。结果还表明，人类和模型在涉及潜在互惠行为的查询时面临共同挑战，提示存在共享的语用敏感性而非模型特定的缺陷。这些发现强调了在LM评估中需要更谨慎的实验设计和编码实践，并挑战了当前模型在语言理解方面固有弱于人类的假设。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在理解英语语句时表现被低估的问题，现有研究未能准确评估人类与模型的理解能力。

**核心思路**：通过设计两种不同的实验条件（允许重读与限制重读），重新评估人类和模型的理解能力，强调实验设计对结果的影响。

**技术框架**：研究采用了预注册的实验设计，比较了人类在不同条件下的反应，并使用了多种模型（如Falcon-180B-Chat、GPT-4、GPT-o1）进行性能评估。

**关键创新**：本研究的创新在于通过限制重读来测试人类理解能力，发现人类在此条件下的表现低于多个大型语言模型，挑战了人类优于模型的传统观点。

**关键设计**：实验中使用了标准化的刺激材料，结合了对模型输出的概率分析和语法评分，确保了评估的系统性和准确性。通过对不同模型的响应进行编码，揭示了模型性能的系统性低估。

## 📊 实验亮点

实验结果显示，当限制重读时，人类的准确率降至73%，低于Falcon-180B-Chat的76%和GPT-4的81%。最新的GPT-o1模型实现了完美的准确率，表明大型语言模型在理解能力上具有显著优势，尤其在特定条件下。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、教育技术和人机交互等。通过更准确地评估语言模型的理解能力，可以推动智能助手、自动翻译和教育工具的发展，提升用户体验和学习效果。

## 📄 摘要（原文）

> Recent claims suggest that large language models (LMs) underperform humans in comprehending minimally complex English statements (Dentella et al., 2024). Here, we revisit those findings and argue that human performance was overestimated, while LLM abilities were underestimated. Using the same stimuli, we report a preregistered study comparing human responses in two conditions: one allowed rereading (replicating the original study), and one that restricted rereading (a more naturalistic comprehension test). Human accuracy dropped significantly when rereading was restricted (73%), falling below that of Falcon-180B-Chat (76%) and GPT-4 (81%). The newer GPT-o1 model achieves perfect accuracy. Results further show that both humans and models are disproportionately challenged by queries involving potentially reciprocal actions (e.g., kissing), suggesting shared pragmatic sensitivities rather than model-specific deficits. Additional analyses using Llama-2-70B log probabilities, a recoding of open-ended model responses, and grammaticality ratings of other sentences reveal systematic underestimation of model performance. We find that GPT-4o can align with either naive or expert grammaticality judgments, depending on prompt framing. These findings underscore the need for more careful experimental design and coding practices in LLM evaluation, and they challenge the assumption that current models are inherently weaker than humans at language comprehension.

