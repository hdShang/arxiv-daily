---
layout: default
title: "NeuroBridge: Using Generative AI to Bridge Cross-neurotype Communication Differences through Neurotypical Perspective-taking"
---

# NeuroBridge: Using Generative AI to Bridge Cross-neurotype Communication Differences through Neurotypical Perspective-taking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23434" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23434v1</a>
  <a href="https://arxiv.org/pdf/2509.23434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23434v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23434v1', 'NeuroBridge: Using Generative AI to Bridge Cross-neurotype Communication Differences through Neurotypical Perspective-taking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rukhshan Haroon, Kyle Wigdor, Katie Yang, Nicole Toumanios, Eileen T. Crehan, Fahad Dogar

**分类**: cs.HC, cs.AI

**发布日期**: 2025-09-27

**DOI**: [10.1145/3663547.3746337](https://doi.org/10.1145/3663547.3746337)

---

## 💡 一句话要点

**NeuroBridge：利用生成式AI和神经典型视角弥合跨神经类型沟通差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经多样性` `自闭症` `大型语言模型` `人机交互` `沟通障碍`

## 📋 核心要点

1. 自闭症个体与神经典型个体间存在沟通障碍，主要原因是双方对彼此的沟通方式缺乏理解，且自闭症个体常被要求适应神经典型规范。
2. NeuroBridge利用大型语言模型模拟自闭症个体的直接沟通风格，并创建跨神经类型沟通场景，让神经典型个体体验和反思。
3. 用户研究表明，NeuroBridge提高了神经典型个体对自闭症沟通方式的理解，并认为AI反馈具有建设性，但同时也指出了AI在残疾表述方面的潜在问题。

## 📝 摘要（中文）

自闭症个体和神经典型个体之间的沟通障碍源于彼此对不同沟通风格的相互不理解。然而，自闭症个体通常被期望适应神经典型规范，这使得互动不真实且精神上令人疲惫。为了帮助纠正这种不平衡，我们构建了NeuroBridge，一个在线平台，利用大型语言模型（LLMs）来模拟：（a）一个直接且字面的AI角色，这是许多自闭症个体常见的风格，以及（b）四个跨神经类型沟通场景，通过该角色和神经典型用户之间基于反馈的对话进行。通过NeuroBridge，神经典型个体可以亲身体验自闭症沟通，并反思他们在塑造跨神经类型互动中的作用。一项针对12名神经典型参与者的用户研究发现，NeuroBridge提高了他们对自闭症患者如何以不同方式解读语言的理解，所有人在完成模拟后都将自闭症描述为一种“需要他人理解”的社会差异。参与者重视其个性化、互动式的形式，并将AI生成的反馈描述为“建设性的”、“逻辑性的”和“非评判性的”。大多数人认为模拟中对自闭症的描绘是准确的，这表明用户可能很容易接受AI生成的对残疾的（错误）表述。最后，我们讨论了AI中残疾表述的设计含义，使NeuroBridge更加个性化的需求，以及LLM在模拟复杂社会场景中的局限性。

## 🔬 方法详解

**问题定义**：论文旨在解决神经典型个体难以理解自闭症个体沟通方式的问题。现有方法主要依赖于传统的教育或培训，但缺乏沉浸式和个性化的体验，难以有效提升神经典型个体对自闭症沟通风格的理解和接纳。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）模拟自闭症个体的沟通风格，创建一个互动式的平台，让神经典型个体通过与AI角色的对话，亲身体验和学习自闭症的沟通方式，从而提高他们的理解和同理心。

**技术框架**：NeuroBridge平台包含两个主要模块：(1) AI角色模拟模块，使用LLM生成具有直接和字面沟通风格的AI角色，模拟自闭症个体的典型沟通方式。(2) 互动场景模块，设计了四个跨神经类型沟通场景，神经典型用户与AI角色进行对话，并获得AI提供的反馈。整个流程是一个反馈驱动的对话过程，用户可以根据AI的反馈调整自己的沟通方式。

**关键创新**：该论文的关键创新在于利用生成式AI技术，特别是大型语言模型，来模拟自闭症个体的沟通风格，并创建一个互动式的学习平台。与传统的教育方法相比，NeuroBridge提供了一种更加沉浸式、个性化和非评判性的学习体验。

**关键设计**：NeuroBridge的关键设计包括：(1) AI角色的个性化设置，确保AI角色能够准确地模拟自闭症个体的沟通风格。(2) 互动场景的设计，需要涵盖常见的跨神经类型沟通挑战，并提供有意义的反馈。(3) LLM的选择和微调，需要选择适合生成自然语言的大型语言模型，并进行微调以更好地模拟自闭症个体的沟通风格。具体的参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

用户研究表明，NeuroBridge显著提高了神经典型个体对自闭症沟通方式的理解。所有参与者在完成模拟后都将自闭症描述为一种“需要他人理解”的社会差异。参与者认为AI生成的反馈是“建设性的”、“逻辑性的”和“非评判性的”，并且大多数人认为模拟中对自闭症的描绘是准确的。这些结果表明NeuroBridge在促进跨神经类型沟通方面具有潜力。

## 🎯 应用场景

NeuroBridge具有广泛的应用前景，可用于提升神经典型个体对自闭症等神经多样性群体的理解和接纳，促进更包容的社会环境。该平台可应用于教育、职场培训等领域，帮助人们更好地与神经多样性个体进行有效沟通和合作。未来，NeuroBridge还可以扩展到其他神经多样性群体，例如ADHD、阅读障碍等。

## 📄 摘要（原文）

> Communication challenges between autistic and neurotypical individuals stem from a mutual lack of understanding of each other's distinct, and often contrasting, communication styles. Yet, autistic individuals are expected to adapt to neurotypical norms, making interactions inauthentic and mentally exhausting for them. To help redress this imbalance, we build NeuroBridge, an online platform that utilizes large language models (LLMs) to simulate: (a) an AI character that is direct and literal, a style common among many autistic individuals, and (b) four cross-neurotype communication scenarios in a feedback-driven conversation between this character and a neurotypical user. Through NeuroBridge, neurotypical individuals gain a firsthand look at autistic communication, and reflect on their role in shaping cross-neurotype interactions. In a user study with 12 neurotypical participants, we find that NeuroBridge improved their understanding of how autistic people may interpret language differently, with all describing autism as a social difference that "needs understanding by others" after completing the simulation. Participants valued its personalized, interactive format and described AI-generated feedback as "constructive", "logical" and "non-judgmental". Most perceived the portrayal of autism in the simulation as accurate, suggesting that users may readily accept AI-generated (mis)representations of disabilities. To conclude, we discuss design implications for disability representation in AI, the need for making NeuroBridge more personalized, and LLMs' limitations in modeling complex social scenarios.

