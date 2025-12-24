---
layout: default
title: "Qianfan-VL: Domain-Enhanced Universal Vision-Language Models"
---

# Qianfan-VL: Domain-Enhanced Universal Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18189" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18189v1</a>
  <a href="https://arxiv.org/pdf/2509.18189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18189v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18189v1', 'Qianfan-VL: Domain-Enhanced Universal Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daxiang Dong, Mingming Zheng, Dong Xu, Bairong Zhuang, Wenyu Zhang, Chunhua Luo, Haoran Wang, Zijian Zhao, Jie Li, Yuxuan Li, Hanjun Zhong, Mengyue Liu, Jieting Chen, Shupeng Li, Lun Tian, Yaping Feng, Xin Li, Donggang Jiang, Yong Chen, Yehua Xu, Duohao Qin, Chen Feng, Dan Wang, Henghua Zhang, Jingjing Ha, Jinhui He, Yanfeng Zhai, Chengxin Zheng, Jiayi Mao, Jiacheng Chen, Ruchang Yao, Ziye Yuan, Jianmin Wu, Guangjun Xie, Dou Shen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-19

**备注**: 12 pages

---

## 💡 一句话要点

**提出Qianfan-VL，通过领域增强技术实现领先的多模态大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `领域增强` `视觉语言模型` `OCR` `文档理解` `长链式思考` `数据合成`

## 📋 核心要点

1. 现有通用视觉语言模型在特定领域表现不足，难以满足企业级应用需求。
2. Qianfan-VL采用多阶段训练和数据合成，增强模型在OCR、文档理解等领域的性能。
3. 实验表明，Qianfan-VL在多个基准测试中达到领先水平，尤其在领域相关任务上提升显著。

## 📝 摘要（中文）

本文介绍了Qianfan-VL，一系列参数规模从30亿到700亿的多模态大语言模型，通过创新的领域增强技术实现了最先进的性能。该方法采用多阶段渐进式训练和高精度数据合成流程，这些技术对于增强领域特定能力同时保持强大的通用性能至关重要。Qianfan-VL在通用基准测试上取得了与领先开源模型相当的结果，并在CCBench、SEEDBench IMG、ScienceQA和MMStar等基准测试上取得了最先进的性能。领域增强策略在OCR和文档理解方面提供了显著优势，这在公共基准测试（OCRBench 873，DocVQA 94.75%）和内部评估中得到了验证。值得注意的是，Qianfan-VL-8B和70B变体结合了长链式思考能力，在数学推理（MathVista 78.6%）和逻辑推理任务上表现出卓越的性能。所有模型完全在百度的昆仑P800芯片上训练，验证了大规模AI基础设施在单个任务上以超过90%的扩展效率在5000个芯片上训练SOTA级多模态模型的能力。这项工作为开发适用于各种企业部署场景的领域增强型多模态模型建立了一种有效的方法。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在通用任务上表现良好，但在OCR、文档理解等特定领域的能力仍有提升空间，难以直接应用于企业级场景。现有方法通常难以兼顾通用性和领域特定性，或者需要大量标注数据，成本较高。

**核心思路**：Qianfan-VL的核心思路是通过领域增强技术，在保持通用性能的同时，显著提升模型在特定领域的表现。通过多阶段渐进式训练和高精度数据合成，使模型能够更好地理解和处理领域相关的信息。

**技术框架**：Qianfan-VL的训练流程主要包括以下几个阶段：1) 预训练阶段：使用大规模通用视觉语言数据集进行预训练，提升模型的通用能力。2) 领域增强阶段：利用高精度数据合成技术生成领域相关的数据，并使用这些数据对模型进行微调，提升模型在特定领域的表现。3) 长链式思考能力增强阶段：针对数学推理和逻辑推理任务，引入长链式思考机制，提升模型的推理能力。

**关键创新**：Qianfan-VL的关键创新在于其领域增强策略，该策略通过多阶段渐进式训练和高精度数据合成，有效地提升了模型在特定领域的性能，同时保持了良好的通用性。此外，模型还引入了长链式思考能力，提升了在复杂推理任务上的表现。

**关键设计**：Qianfan-VL采用了多阶段训练策略，包括预训练、领域增强和长链式思考能力增强。在领域增强阶段，使用了高精度数据合成技术，例如，针对OCR任务，合成了包含各种字体、布局和噪声的文档图像。在长链式思考能力增强阶段，使用了特定的损失函数和训练技巧，鼓励模型生成更长的推理链。

## 📊 实验亮点

Qianfan-VL在OCRBench上达到873分，DocVQA上达到94.75%，MathVista上达到78.6%，均取得了领先的性能。与现有开源模型相比，Qianfan-VL在领域相关任务上取得了显著的提升，验证了领域增强策略的有效性。此外，该模型在5000个昆仑P800芯片上实现了超过90%的扩展效率，证明了其在大规模AI基础设施上的可训练性。

## 🎯 应用场景

Qianfan-VL可广泛应用于企业级场景，例如智能文档处理、财务报表分析、法律文书理解等。通过提升模型在特定领域的性能，可以有效降低人工成本，提高工作效率。未来，该模型有望在更多领域得到应用，例如医疗影像分析、工业质检等。

## 📄 摘要（原文）

> We present Qianfan-VL, a series of multimodal large language models ranging from 3B to 70B parameters, achieving state-of-the-art performance through innovative domain enhancement techniques. Our approach employs multi-stage progressive training and high-precision data synthesis pipelines, which prove to be critical technologies for enhancing domain-specific capabilities while maintaining strong general performance. Qianfan-VL achieves comparable results to leading open-source models on general benchmarks, with state-of-the-art performance on benchmarks such as CCBench, SEEDBench IMG, ScienceQA, and MMStar. The domain enhancement strategy delivers significant advantages in OCR and document understanding, validated on both public benchmarks (OCRBench 873, DocVQA 94.75%) and in-house evaluations. Notably, Qianfan-VL-8B and 70B variants incorporate long chain-of-thought capabilities, demonstrating superior performance on mathematical reasoning (MathVista 78.6%) and logical inference tasks. All models are trained entirely on Baidu's Kunlun P800 chips, validating the capability of large-scale AI infrastructure to train SOTA-level multimodal models with over 90% scaling efficiency on 5000 chips for a single task. This work establishes an effective methodology for developing domain-enhanced multimodal models suitable for diverse enterprise deployment scenarios.

