---
layout: default
title: PILAR: Personalizing Augmented Reality Interactions with LLM-based Human-Centric and Trustworthy Explanations for Daily Use Cases
---

# PILAR: Personalizing Augmented Reality Interactions with LLM-based Human-Centric and Trustworthy Explanations for Daily Use Cases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17172" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17172v1</a>
  <a href="https://arxiv.org/pdf/2512.17172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17172v1', 'PILAR: Personalizing Augmented Reality Interactions with LLM-based Human-Centric and Trustworthy Explanations for Daily Use Cases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ripan Kumar Kundu, Istiak Ahmed, Khaza Anuarul Hoque

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-19

**备注**: Published in the 2025 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)

**DOI**: [10.1109/ISMAR-Adjunct68609.2025.00060](https://doi.org/10.1109/ISMAR-Adjunct68609.2025.00060)

---

## 💡 一句话要点

**PILAR：利用LLM生成以人为本的可信解释，个性化增强现实交互，应用于日常场景。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增强现实` `可解释人工智能` `大型语言模型` `人机交互` `个性化推荐`

## 📋 核心要点

1. 现有XAI方法难以提供动态、个性化、以人为本的AR交互解释，导致用户体验不佳。
2. PILAR利用LLM生成上下文感知和个性化的解释，统一解决不同解释维度的问题，提升用户信任。
3. 用户研究表明，与传统方法相比，PILAR使任务完成速度提升40%，显著提高用户满意度和易用性。

## 📝 摘要（中文）

人工智能驱动的增强现实（AR）系统日益融入日常生活，对实时用户交互的可解释性需求也随之增长。传统的XAI方法依赖于基于特征或示例的解释，难以提供动态、特定于上下文、个性化和以人为本的洞察。这些方法通常使用不同的解释技术来解决不同的可解释性维度，导致不切实际和碎片化的AR交互体验。为解决此问题，我们提出了PILAR，一种利用预训练大型语言模型（LLM）生成上下文感知、个性化解释的新框架，在实时AI驱动的AR系统中提供更直观和可信的体验。与传统方法不同，PILAR采用统一的基于LLM的方法，动态地调整解释以满足用户的需求，从而增强信任和参与度。我们在一个真实的AR应用（例如，个性化食谱推荐）中实现了PILAR概念，这是一个开源原型，集成了实时对象检测、食谱推荐和基于LLM的个性化食谱解释，该解释基于用户的饮食偏好。通过一项用户研究，我们评估了PILAR的有效性，其中16名参与者执行基于AR的食谱推荐任务，并将基于LLM的解释界面与传统的基于模板的界面进行比较。结果表明，基于LLM的界面显著提高了用户的性能和体验，参与者完成任务的速度提高了40%，并且报告了更高的满意度、易用性和感知透明度。

## 🔬 方法详解

**问题定义**：现有增强现实(AR)系统中的可解释人工智能(XAI)方法，如基于特征或示例的解释，无法提供动态、上下文相关、个性化和以人为本的解释。这些方法通常需要多种技术来处理不同的解释维度（例如，何时、什么、如何），导致用户体验不连贯和不自然。因此，如何为AR用户提供无缝、可信且易于理解的解释是一个关键问题。

**核心思路**：PILAR的核心思路是利用预训练的大型语言模型(LLM)来生成上下文感知的、个性化的解释。LLM具有强大的语言理解和生成能力，可以根据用户的具体需求和场景，动态地调整解释的内容和形式。这种方法旨在提供更直观、更可信的AR交互体验，增强用户的信任感和参与度。

**技术框架**：PILAR框架包含以下主要模块：1) **实时对象检测**：用于识别AR场景中的物体。2) **食谱推荐**：根据检测到的物体和用户的饮食偏好，推荐相关的食谱。3) **LLM解释生成**：利用LLM根据用户的偏好和食谱内容，生成个性化的解释。整个流程是：用户通过AR设备与环境交互，系统检测到相关对象后，推荐食谱，然后LLM生成针对该食谱的个性化解释，并呈现给用户。

**关键创新**：PILAR的关键创新在于使用统一的LLM来处理所有解释维度，而不是像传统方法那样使用多种技术。这种统一的方法可以生成更连贯、更自然的解释，并更好地适应用户的需求。此外，PILAR还关注个性化，根据用户的饮食偏好定制解释，从而提高用户的信任感和满意度。

**关键设计**：PILAR使用预训练的LLM，并通过微调来适应特定的AR应用场景。在食谱推荐应用中，系统会收集用户的饮食偏好信息，并将其作为LLM的输入，以生成个性化的解释。具体的提示工程（prompt engineering）策略和LLM的选择（例如，GPT-3, PaLM等）是影响解释质量的关键因素。论文中没有明确说明具体的损失函数或网络结构，但强调了LLM的微调过程。

## 📊 实验亮点

用户研究表明，与传统的基于模板的解释界面相比，基于LLM的PILAR界面显著提高了用户的性能和体验。具体来说，参与者在使用PILAR界面时，完成任务的速度提高了40%，并且报告了更高的满意度、易用性和感知透明度。这些结果表明，LLM可以有效地生成更有效、更令人满意的AR解释。

## 🎯 应用场景

PILAR框架具有广泛的应用前景，例如个性化教育、智能家居、远程医疗等。在教育领域，可以为学生提供个性化的学习辅导；在智能家居领域，可以帮助用户更好地理解和控制智能设备；在远程医疗领域，可以为患者提供更清晰的诊断解释。该研究有助于推动人机交互的智能化和个性化发展。

## 📄 摘要（原文）

> Artificial intelligence (AI)-driven augmented reality (AR) systems are becoming increasingly integrated into daily life, and with this growth comes a greater need for explainability in real-time user interactions. Traditional explainable AI (XAI) methods, which often rely on feature-based or example-based explanations, struggle to deliver dynamic, context-specific, personalized, and human-centric insights for everyday AR users. These methods typically address separate explainability dimensions (e.g., when, what, how) with different explanation techniques, resulting in unrealistic and fragmented experiences for seamless AR interactions. To address this challenge, we propose PILAR, a novel framework that leverages a pre-trained large language model (LLM) to generate context-aware, personalized explanations, offering a more intuitive and trustworthy experience in real-time AI-powered AR systems. Unlike traditional methods, which rely on multiple techniques for different aspects of explanation, PILAR employs a unified LLM-based approach that dynamically adapts explanations to the user's needs, fostering greater trust and engagement. We implement the PILAR concept in a real-world AR application (e.g., personalized recipe recommendations), an open-source prototype that integrates real-time object detection, recipe recommendation, and LLM-based personalized explanations of the recommended recipes based on users' dietary preferences. We evaluate the effectiveness of PILAR through a user study with 16 participants performing AR-based recipe recommendation tasks, comparing an LLM-based explanation interface to a traditional template-based one. Results show that the LLM-based interface significantly enhances user performance and experience, with participants completing tasks 40% faster and reporting greater satisfaction, ease of use, and perceived transparency.

