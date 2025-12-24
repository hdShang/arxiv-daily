---
layout: default
title: InteractAnything: Zero-shot Human Object Interaction Synthesis via LLM Feedback and Object Affordance Parsing
---

# InteractAnything: Zero-shot Human Object Interaction Synthesis via LLM Feedback and Object Affordance Parsing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24315" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24315v1</a>
  <a href="https://arxiv.org/pdf/2505.24315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24315v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24315v1', 'InteractAnything: Zero-shot Human Object Interaction Synthesis via LLM Feedback and Object Affordance Parsing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinlu Zhang, Yixin Chen, Zan Wang, Jie Yang, Yizhou Wang, Siyuan Huang

**分类**: cs.CV

**发布日期**: 2025-05-30

**备注**: CVPR 2025

---

## 💡 一句话要点

**提出InteractAnything以解决零样本人机交互合成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `3D生成` `零样本学习` `大型语言模型` `图像解析` `优化算法` `虚拟现实`

## 📋 核心要点

1. 现有方法在从文本生成新的人机交互方面存在困难，尤其是在处理开放集对象时，面临人机关系推理和姿态合成的挑战。
2. 本文提出了一种零样本3D HOI生成框架，利用大型语言模型推断人机关系，并结合预训练的2D图像扩散模型进行对象解析。
3. 实验结果表明，该方法在交互细致程度和开放集3D对象处理能力上显著优于现有技术，展示了良好的应用潜力。

## 📝 摘要（中文）

近年来，3D人类感知生成取得了显著进展，但现有方法在从文本生成新的人机交互（HOI）方面仍面临挑战，尤其是对于开放集对象。本文提出了一种新颖的零样本3D HOI生成框架，利用大规模预训练模型的知识，无需在特定数据集上训练。通过大型语言模型（LLMs）推断人机关系，初始化对象属性并指导优化过程。利用预训练的2D图像扩散模型解析未见对象并提取接触点，避免了现有3D资产知识的限制。最终，通过细致的优化生成精细、自然的交互，确保3D对象与涉及身体部位（如手）的真实接触。大量实验验证了该方法的有效性，特别是在交互的细致程度和处理开放集3D对象的能力上。

## 🔬 方法详解

**问题定义**：本文旨在解决从文本生成新的人机交互（HOI）时的挑战，特别是开放集对象的处理。现有方法在精确的人机关系推理、物体可用性解析和姿态合成上存在不足。

**核心思路**：通过利用大型语言模型（LLMs）推断人机关系，初始化对象属性并指导优化过程，避免了对特定数据集的依赖。

**技术框架**：整体架构包括三个主要模块：首先，利用LLMs推断人机关系；其次，使用预训练的2D图像扩散模型解析未见对象；最后，通过多视角样本生成初始人类姿态，并进行细致优化以生成自然交互。

**关键创新**：该研究的核心创新在于结合LLMs的反馈与物体可用性解析，能够在没有特定数据集的情况下生成高质量的3D HOI，显著提升了交互的细致程度。

**关键设计**：在技术细节上，采用了多视角样本生成策略，设计了特定的损失函数以确保3D对象与身体部位的真实接触，优化过程中引入了人类反馈以提升生成质量。

## 📊 实验亮点

实验结果显示，本文方法在交互细致程度上相比于现有技术有显著提升，尤其在处理开放集3D对象时，生成的交互质量更高，具体性能数据表明，交互的自然性和真实感均有明显改善。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和人机交互设计等。通过实现高质量的3D人机交互合成，能够提升用户体验，推动相关领域的技术进步和应用创新。未来，该方法可能在自动化内容生成和智能机器人领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in 3D human-aware generation have made significant progress. However, existing methods still struggle with generating novel Human Object Interaction (HOI) from text, particularly for open-set objects. We identify three main challenges of this task: precise human-object relation reasoning, affordance parsing for any object, and detailed human interaction pose synthesis aligning description and object geometry. In this work, we propose a novel zero-shot 3D HOI generation framework without training on specific datasets, leveraging the knowledge from large-scale pre-trained models. Specifically, the human-object relations are inferred from large language models (LLMs) to initialize object properties and guide the optimization process. Then we utilize a pre-trained 2D image diffusion model to parse unseen objects and extract contact points, avoiding the limitations imposed by existing 3D asset knowledge. The initial human pose is generated by sampling multiple hypotheses through multi-view SDS based on the input text and object geometry. Finally, we introduce a detailed optimization to generate fine-grained, precise, and natural interaction, enforcing realistic 3D contact between the 3D object and the involved body parts, including hands in grasping. This is achieved by distilling human-level feedback from LLMs to capture detailed human-object relations from the text instruction. Extensive experiments validate the effectiveness of our approach compared to prior works, particularly in terms of the fine-grained nature of interactions and the ability to handle open-set 3D objects.

