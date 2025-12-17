---
layout: default
title: DreamOmni2: Multimodal Instruction-based Editing and Generation
---

# DreamOmni2: Multimodal Instruction-based Editing and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06679" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06679v1</a>
  <a href="https://arxiv.org/pdf/2510.06679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06679v1" onclick="toggleFavorite(this, '2510.06679v1', 'DreamOmni2: Multimodal Instruction-based Editing and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Xia, Bohao Peng, Yuechen Zhang, Junjia Huang, Jiyang Liu, Jingyao Li, Haoru Tan, Sitong Wu, Chengyao Wang, Yitong Wang, Xinglong Wu, Bei Yu, Jiaya Jia

**分类**: cs.CV

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**DreamOmni2：提出多模态指令驱动的图像编辑与生成框架，扩展应用场景。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `图像编辑` `图像生成` `指令驱动` `抽象概念` `视觉语言模型` `数据合成`

## 📋 核心要点

1. 现有指令驱动图像编辑依赖文本指令，缺乏细节控制，而主题驱动生成局限于具体对象，无法处理抽象概念。
2. DreamOmni2提出多模态指令驱动的编辑与生成，支持文本和图像指令，扩展到抽象概念，增强了实用性。
3. 通过特征混合的数据合成流程和索引编码的位置编码移位方案，DreamOmni2在实验中取得了显著成果。

## 📝 摘要（中文）

指令驱动的图像编辑和主题驱动的图像生成近年来备受关注，但两者在满足实际用户需求方面仍存在局限性。指令驱动的编辑仅依赖语言指令，难以捕捉具体的编辑细节，需要参考图像。而主题驱动的生成仅限于组合具体的对象或人物，忽略了更广泛、抽象的概念。为了解决这些挑战，我们提出了两种新的任务：多模态指令驱动的编辑和生成。这些任务支持文本和图像指令，并将范围扩展到具体和抽象概念，大大增强了它们的实际应用。我们引入了DreamOmni2，解决了数据创建和模型框架设计两个主要挑战。我们的数据合成流程包括三个步骤：（1）使用特征混合方法创建抽象和具体概念的提取数据，（2）使用编辑和提取模型生成多模态指令驱动的编辑训练数据，以及（3）进一步应用提取模型来创建多模态指令驱动的编辑训练数据。在框架方面，为了处理多图像输入，我们提出了一种索引编码和位置编码移位方案，这有助于模型区分图像并避免像素混淆。此外，我们引入了与VLM和我们的生成/编辑模型的联合训练，以更好地处理复杂的指令。此外，我们为这两个新任务提出了全面的基准，以推动它们的发展。实验表明，DreamOmni2取得了令人印象深刻的结果。模型和代码将会开源。

## 🔬 方法详解

**问题定义**：现有指令驱动的图像编辑方法主要依赖于文本指令，难以精确控制编辑细节，需要额外的参考图像。同时，主题驱动的图像生成方法通常只能处理具体的对象或人物，无法生成抽象的概念，限制了其应用范围。因此，需要一种能够同时处理文本和图像指令，并能够生成和编辑抽象概念的图像生成和编辑方法。

**核心思路**：DreamOmni2的核心思路是利用多模态信息（文本和图像）作为指令，指导图像的编辑和生成。通过引入图像指令，可以更精确地表达用户的意图，从而生成更符合用户需求的图像。同时，通过对抽象概念进行建模，可以扩展图像生成和编辑的应用范围。

**技术框架**：DreamOmni2的整体框架包括数据合成和模型训练两个主要部分。数据合成部分，首先使用特征混合方法创建抽象和具体概念的提取数据，然后利用编辑和提取模型生成多模态指令驱动的编辑训练数据，最后进一步应用提取模型来创建多模态指令驱动的编辑训练数据。模型训练部分，为了处理多图像输入，提出了一种索引编码和位置编码移位方案，以区分图像并避免像素混淆。此外，还引入了与VLM和生成/编辑模型的联合训练，以更好地处理复杂的指令。

**关键创新**：DreamOmni2的关键创新在于提出了多模态指令驱动的图像编辑和生成任务，并设计了相应的数据合成和模型训练方法。与现有方法相比，DreamOmni2能够同时处理文本和图像指令，并能够生成和编辑抽象概念的图像。此外，提出的索引编码和位置编码移位方案以及与VLM的联合训练也提高了模型的性能。

**关键设计**：在数据合成方面，使用了特征混合方法来创建抽象和具体概念的提取数据。在模型训练方面，使用了索引编码和位置编码移位方案来处理多图像输入，并引入了与VLM的联合训练。具体的损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

DreamOmni2在多模态指令驱动的图像编辑和生成任务上取得了令人印象深刻的结果。论文提出了全面的基准，并进行了实验验证，证明了DreamOmni2的有效性。具体的性能数据和提升幅度在摘要和论文正文中未明确给出，属于未知信息。模型和代码将会开源，方便研究人员进行进一步的研究和应用。

## 🎯 应用场景

DreamOmni2具有广泛的应用前景，例如：艺术创作、广告设计、虚拟现实、游戏开发等。用户可以通过文本和图像指令，轻松地编辑和生成各种图像，从而提高创作效率和质量。此外，DreamOmni2还可以应用于教育领域，帮助学生更好地理解抽象概念。

## 📄 摘要（原文）

> Recent advancements in instruction-based image editing and subject-driven generation have garnered significant attention, yet both tasks still face limitations in meeting practical user needs. Instruction-based editing relies solely on language instructions, which often fail to capture specific editing details, making reference images necessary. Meanwhile, subject-driven generation is limited to combining concrete objects or people, overlooking broader, abstract concepts. To address these challenges, we propose two novel tasks: multimodal instruction-based editing and generation. These tasks support both text and image instructions and extend the scope to include both concrete and abstract concepts, greatly enhancing their practical applications. We introduce DreamOmni2, tackling two primary challenges: data creation and model framework design. Our data synthesis pipeline consists of three steps: (1) using a feature mixing method to create extraction data for both abstract and concrete concepts, (2) generating multimodal instruction-based editing training data using the editing and extraction models, and (3) further applying the extraction model to create training data for multimodal instruction-based editing. For the framework, to handle multi-image input, we propose an index encoding and position encoding shift scheme, which helps the model distinguish images and avoid pixel confusion. Additionally, we introduce joint training with the VLM and our generation/editing model to better process complex instructions. In addition, we have proposed comprehensive benchmarks for these two new tasks to drive their development. Experiments show that DreamOmni2 has achieved impressive results. Models and codes will be released.

