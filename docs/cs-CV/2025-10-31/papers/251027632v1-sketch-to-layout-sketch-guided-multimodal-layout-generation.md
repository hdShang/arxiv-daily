---
layout: default
title: Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation
---

# Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27632" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27632v1</a>
  <a href="https://arxiv.org/pdf/2510.27632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27632v1" onclick="toggleFavorite(this, '2510.27632v1', 'Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Riccardo Brioschi, Aleksandr Alekseev, Emanuele Nevali, Berkay Döner, Omar El Malki, Blagoj Mitrevski, Leandro Kieliger, Mark Collier, Andrii Maksai, Jesse Berent, Claudiu Musat, Efi Kokiopoulou

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-31

**备注**: 15 pages, 18 figures, GitHub link: https://github.com/google-deepmind/sketch_to_layout, accept at ICCV 2025 Workshop (HiGen)

**🔗 代码/项目**: [GITHUB](https://github.com/google-deepmind/sketch_to_layout)

---

## 💡 一句话要点

**提出Sketch-to-Layout框架，利用草图引导多模态布局生成，提升设计体验。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `布局生成` `草图引导` `多模态学习` `Transformer` `合成数据` `用户约束` `图形设计`

## 📋 核心要点

1. 现有布局生成方法依赖复杂的用户约束，降低了易用性，难以满足用户直观的设计需求。
2. 提出Sketch-to-Layout框架，利用用户草图作为直观约束，指导多模态Transformer生成高质量布局。
3. 通过合成草图数据进行训练，并在PubLayNet等数据集上验证，超越现有约束方法，提升设计体验。

## 📝 摘要（中文）

图形布局生成是一个新兴的研究领域，专注于生成从海报设计到文档等美观的布局。虽然最近的研究探索了结合用户约束来指导布局生成的方法，但这些约束通常需要复杂的规范，从而降低了可用性。我们引入了一种创新方法，利用用户提供的草图作为直观的约束，并从经验上证明了这种新指导方法的有效性，从而将草图到布局问题确立为一个有前景但目前尚未充分探索的研究方向。为了解决草图到布局问题，我们提出了一种基于多模态Transformer的解决方案，使用草图和内容资产作为输入来生成高质量的布局。由于从人工标注者那里收集草图训练数据来训练我们的模型成本很高，因此我们引入了一种新颖而有效的方法来大规模地合成生成训练草图。我们在三个公开可用的数据集PubLayNet、DocLayNet和SlidesVQA上训练和评估我们的模型，结果表明它优于最先进的基于约束的方法，同时提供了更直观的设计体验。为了方便未来的草图到布局研究，我们发布了上述公共数据集的O(200k)个合成生成的草图。

## 🔬 方法详解

**问题定义**：论文旨在解决图形布局生成中用户约束复杂、不易用的问题。现有方法需要用户进行复杂的参数设置或规则定义，无法直接表达设计意图，限制了布局生成系统的可用性和用户体验。

**核心思路**：论文的核心思路是利用用户提供的草图作为布局生成的直观约束。草图能够简洁明了地表达用户对布局的期望，避免了复杂的参数设置。通过将草图与内容资产相结合，模型可以生成符合用户意图且美观的布局。

**技术框架**：该方法采用基于Transformer的多模态架构。输入包括用户草图和内容资产（例如文本、图像）。模型首先对草图和内容进行编码，然后通过Transformer进行融合和布局预测。输出是布局中各个元素的位置和大小等信息。整体流程包括草图输入、内容输入、特征编码、Transformer融合、布局预测等阶段。

**关键创新**：该方法最重要的创新点在于将用户草图作为布局生成的直接约束。此外，为了解决草图数据稀缺的问题，论文提出了一种高效的合成草图生成方法，能够大规模生成训练数据。这种合成数据生成方法是训练模型的重要保障。

**关键设计**：模型采用Transformer架构，具体网络结构细节未详细描述。损失函数的设计目标是使生成的布局与用户草图尽可能一致，同时保证布局的美观性和合理性。合成草图生成方法可能涉及随机扰动、形状组合等技术，具体细节未知。

## 📊 实验亮点

该模型在PubLayNet、DocLayNet和SlidesVQA三个数据集上进行了评估，实验结果表明，该方法优于现有的基于约束的布局生成方法。具体的性能提升数据未知，但论文强调了该方法在提供更直观设计体验方面的优势。

## 🎯 应用场景

该研究成果可应用于海报设计、文档排版、幻灯片制作等领域。用户可以通过简单的草图快速生成符合需求的布局，降低设计门槛，提高设计效率。未来，该技术有望集成到各种设计软件和平台中，赋能更广泛的用户群体。

## 📄 摘要（原文）

> Graphic layout generation is a growing research area focusing on generating aesthetically pleasing layouts ranging from poster designs to documents. While recent research has explored ways to incorporate user constraints to guide the layout generation, these constraints often require complex specifications which reduce usability. We introduce an innovative approach exploiting user-provided sketches as intuitive constraints and we demonstrate empirically the effectiveness of this new guidance method, establishing the sketch-to-layout problem as a promising research direction, which is currently under-explored. To tackle the sketch-to-layout problem, we propose a multimodal transformer-based solution using the sketch and the content assets as inputs to produce high quality layouts. Since collecting sketch training data from human annotators to train our model is very costly, we introduce a novel and efficient method to synthetically generate training sketches at scale. We train and evaluate our model on three publicly available datasets: PubLayNet, DocLayNet and SlidesVQA, demonstrating that it outperforms state-of-the-art constraint-based methods, while offering a more intuitive design experience. In order to facilitate future sketch-to-layout research, we release O(200k) synthetically-generated sketches for the public datasets above. The datasets are available at https://github.com/google-deepmind/sketch_to_layout.

