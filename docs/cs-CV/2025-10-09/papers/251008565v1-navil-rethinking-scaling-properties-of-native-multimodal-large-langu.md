---
layout: default
title: NaViL: Rethinking Scaling Properties of Native Multimodal Large Language Models under Data Constraints
---

# NaViL: Rethinking Scaling Properties of Native Multimodal Large Language Models under Data Constraints

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08565" target="_blank" class="toolbar-btn">arXiv: 2510.08565v1</a>
    <a href="https://arxiv.org/pdf/2510.08565.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08565v1" 
            onclick="toggleFavorite(this, '2510.08565v1', 'NaViL: Rethinking Scaling Properties of Native Multimodal Large Language Models under Data Constraints')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Changyao Tian, Hao Li, Gen Luo, Xizhou Zhu, Weijie Su, Hanming Deng, Jinguo Zhu, Jie Shao, Ziran Zhu, Yunpeng Liu, Lewei Lu, Wenhai Wang, Hongsheng Li, Jifeng Dai

**分类**: cs.CV

**发布日期**: 2025-10-09

**备注**: Accepted by NeurIPS 2025. 22 pages, link: https://github.com/OpenGVLab/NaViL

---

## 💡 一句话要点

**NaViL：数据约束下原生多模态大语言模型缩放特性的再思考**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `原生训练` `数据约束` `缩放特性` `视觉语言模型`

## 📋 核心要点

1. 现有MLLM依赖组合训练，视觉编码器和LLM分离训练，限制了多模态缩放特性的探索。
2. 论文提出原生端到端训练MLLM，研究数据约束下的设计空间和缩放特性，优化元架构。
3. 实验表明，提出的NaViL在多个多模态基准上表现出竞争性能，并为未来研究提供见解。

## 📝 摘要（中文）

现有的多模态大语言模型（MLLMs）通常采用组合训练范式，即通过连续的多模态预训练将预训练的视觉编码器与预训练的LLM连接起来。然而，由于分离的训练方式，这种范式的多模态缩放特性难以探索。本文着重研究MLLMs的原生端到端训练，并在实际的数据约束环境下系统地研究其设计空间和缩放特性。通过对MLLM中各种选择的仔细研究，我们获得了最佳的元架构，该架构能够最好地平衡性能和训练成本。此外，我们进一步探索了原生MLLM的缩放特性，并表明视觉编码器和LLM之间存在正相关的缩放关系。基于这些发现，我们提出了一个名为NaViL的原生MLLM，并结合了一个简单且经济高效的方案。在14个多模态基准上的实验结果证实了NaViL相对于现有MLLM的竞争性能。除此之外，我们的发现和结果为未来原生MLLM的研究提供了深入的见解。

## 🔬 方法详解

**问题定义**：现有MLLM通常采用组合训练，即先分别预训练视觉编码器和LLM，然后通过多模态预训练将二者连接。这种方式限制了对MLLM整体缩放特性的研究，尤其是在数据受限的情况下，如何平衡视觉和语言模型的规模以达到最佳性能是一个挑战。

**核心思路**：论文的核心思路是采用原生端到端训练MLLM，将视觉编码器和LLM作为一个整体进行训练。通过系统地探索MLLM的设计空间，找到在数据约束下性能和训练成本的最佳平衡点。同时，研究视觉编码器和LLM之间的缩放关系，指导模型设计。

**技术框架**：NaViL的整体架构包含视觉编码器、多模态连接器和LLM。视觉编码器负责提取图像特征，多模态连接器将视觉特征映射到LLM的输入空间，LLM负责生成文本。训练过程是端到端的，即同时优化视觉编码器、连接器和LLM的参数。

**关键创新**：关键创新在于对原生MLLM的系统性研究，包括对不同视觉编码器、多模态连接器和LLM的组合进行评估，以及对视觉和语言模型缩放关系的探索。通过实验确定了最佳的元架构，并在数据约束下实现了具有竞争力的性能。

**关键设计**：论文中一个关键的设计是探索了不同视觉编码器（如ViT、ConvNeXt）和LLM（如LLaMA）的组合。此外，还研究了不同的多模态连接器，如线性层、MLP等。通过实验确定了在数据约束下性能最佳的组合方式。损失函数采用标准的语言模型损失，即最大化生成文本的概率。

## 📊 实验亮点

NaViL在14个多模态基准测试中表现出与现有MLLM相当甚至更优的性能。例如，在VQA任务上，NaViL取得了与现有SOTA模型相近的结果，同时训练成本更低。研究还揭示了视觉编码器和LLM之间的正相关缩放关系，为未来MLLM的设计提供了指导。

## 🎯 应用场景

该研究成果可应用于各种需要理解图像和文本的多模态任务，例如图像描述、视觉问答、视觉推理等。通过优化MLLM的架构和训练方式，可以提高模型在数据受限场景下的性能，降低训练成本，加速多模态AI的应用落地。未来，该研究可以进一步扩展到视频理解、机器人控制等更复杂的领域。

## 📄 摘要（原文）

> Compositional training has been the de-facto paradigm in existing Multimodal Large Language Models (MLLMs), where pre-trained vision encoders are connected with pre-trained LLMs through continuous multimodal pre-training. However, the multimodal scaling property of this paradigm remains difficult to explore due to the separated training. In this paper, we focus on the native training of MLLMs in an end-to-end manner and systematically study its design space and scaling property under a practical setting, i.e., data constraint. Through careful study of various choices in MLLM, we obtain the optimal meta-architecture that best balances performance and training cost. After that, we further explore the scaling properties of the native MLLM and indicate the positively correlated scaling relationship between visual encoders and LLMs. Based on these findings, we propose a native MLLM called NaViL, combined with a simple and cost-effective recipe. Experimental results on 14 multimodal benchmarks confirm the competitive performance of NaViL against existing MLLMs. Besides that, our findings and results provide in-depth insights for the future study of native MLLMs.

