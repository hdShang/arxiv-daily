---
layout: default
title: "DiSC-AMC: Token- and Parameter-Efficient Discretized Statistics In-Context Automatic Modulation Classification"
---

# DiSC-AMC: Token- and Parameter-Efficient Discretized Statistics In-Context Automatic Modulation Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00316" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00316v1</a>
  <a href="https://arxiv.org/pdf/2510.00316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00316v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00316v1', 'DiSC-AMC: Token- and Parameter-Efficient Discretized Statistics In-Context Automatic Modulation Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Rostami, Atik Faysal, Reihaneh Gh. Roshan, Huaxia Wang, Nikhil Muralidhar, Yu-Dong Yao

**分类**: cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**DiSC-AMC：面向自动调制分类，提出token和参数高效的离散化统计上下文学习方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动调制分类` `大型语言模型` `上下文学习` `离散化` `特征选择`

## 📋 核心要点

1. 现有基于LLM的自动调制分类方法依赖于长上下文提示和大型模型，导致部署成本高昂。
2. DiSC-AMC通过离散化统计特征、精简上下文示例和优化提示模板，显著降低了token和参数需求。
3. 实验表明，DiSC-AMC在保持甚至提升分类准确率的同时，推理成本降低超过2倍，更易于实际应用。

## 📝 摘要（中文）

本文针对大型语言模型(LLM)在自动调制分类(AMC)中，上下文提示过长和模型过大的问题，提出了一种token和参数高效的离散化统计上下文自动调制分类方法(DiSC-AMC)。该方法通过以下方式实现高效：(i)将高阶统计量和累积量离散化为紧凑的符号token；(ii)通过轻量级的k-top神经预过滤器修剪示例列表，并使用从先前LLM响应中提取的理由来过滤误导性/低影响的特征；(iii)通过校准的提示模板强制执行仅标签预测。这些改变显著减少了输入/输出token和模型参数，同时保持了具有竞争力的准确性。在噪声下的十种调制类型的合成AMC上，一个7B参数的DeepSeek-R1-Distill-Qwen基线实现了5.2%的准确率，而我们的系统，使用一个大约5B参数的Gemini-2.5-Flash模型，达到了45.5%的准确率。结果表明，仔细的离散化和上下文选择可以将推理成本降低2倍以上，同时保留基于提示的AMC的优势，并实现实际的环内使用。

## 🔬 方法详解

**问题定义**：现有基于大型语言模型（LLM）的自动调制分类（AMC）方法，虽然能够在开放集场景下工作，但依赖于精心设计的上下文提示。这些提示通常很长，需要大量的token，并且依赖于大型模型，导致计算成本高昂，难以在实际环内部署。现有方法的痛点在于token效率和参数效率不足。

**核心思路**：DiSC-AMC的核心思路是通过离散化高阶统计量和累积量，将其转化为紧凑的符号token，从而减少输入token的数量。同时，通过神经预过滤器和基于LLM理由的特征选择，精简上下文示例，降低模型需要处理的信息量。此外，通过校准的提示模板，强制模型进行仅标签预测，进一步减少输出token的数量。这样，在不显著降低分类准确率的前提下，显著降低了token和参数需求。

**技术框架**：DiSC-AMC的整体框架包含以下几个主要阶段：1) **特征提取与离散化**：从接收到的信号中提取高阶统计量和累积量，并将这些连续值离散化为符号token。2) **上下文示例选择**：使用轻量级的k-top神经预过滤器从候选示例列表中选择最相关的示例。3) **特征过滤**：利用先前LLM响应中提取的理由，过滤掉误导性或低影响的特征。4) **提示构建**：使用校准的提示模板，将离散化的特征和选择的示例组合成上下文提示。5) **LLM推理**：将构建的提示输入LLM，获得调制类型的预测结果。

**关键创新**：DiSC-AMC的关键创新在于将高阶统计量和累积量离散化为符号token，以及利用LLM的理由进行特征选择。与现有方法相比，DiSC-AMC不需要直接将原始信号或连续的统计特征输入LLM，而是使用更紧凑的符号表示，从而显著降低了输入token的数量。此外，利用LLM的理由进行特征选择，可以更有效地过滤掉不相关的特征，提高分类准确率。

**关键设计**：关于离散化，具体如何选择离散化的区间和数量，论文中可能涉及。神经预过滤器的具体结构和训练方式，以及如何从LLM的响应中提取理由，都是关键的设计细节。校准的提示模板的设计也至关重要，需要确保模型能够准确理解提示的含义，并进行正确的预测。具体的参数设置、损失函数、网络结构等细节，需要参考论文原文。

## 📊 实验亮点

DiSC-AMC在合成AMC数据集上取得了显著的性能提升。使用约5B参数的Gemini-2.5-Flash模型，DiSC-AMC达到了45.5%的准确率，而使用7B参数的DeepSeek-R1-Distill-Qwen基线仅达到5.2%的准确率。这表明DiSC-AMC在保持甚至提升分类准确率的同时，显著降低了模型参数和推理成本。

## 🎯 应用场景

DiSC-AMC可应用于无线通信、频谱感知、信号情报等领域。通过降低LLM在AMC中的计算成本，使得在资源受限的设备上进行实时调制分类成为可能。该方法有助于提高无线通信系统的效率和安全性，并为未来的智能无线网络提供技术支持。

## 📄 摘要（原文）

> Large Language Models (LLMs) can perform Automatic Modulation Classification (AMC) in an open-set manner without LLM fine-tuning when equipped with carefully designed in-context prompts~\cite{rostami2025plug}. Building on this prior work, we target the practical bottlenecks of long prompt contexts and large model sizes that impede in-the-loop deployment. We present Discretized Statistics in-Context Automatic Modulation Classification (DiSC-AMC), a token- and parameter-efficient variant that: (i) discretizes higher-order statistics and cumulants into compact symbolic tokens, (ii) prunes the exemplar list via a lightweight k-top neural prefilter and filters misleading/low-impact features using rationales extracted from prior LLM responses, and (iii) enforces label-only predictions through a calibrated prompt template. Together, these changes reduce both input/output tokens and the model parameter footprint by more than half while maintaining competitive accuracy. On synthetic AMC with ten modulation types under noise, a 7B \textit{DeepSeek-R1-Distill-Qwen} baseline achieves 5.2% accuracy, whereas our system, using an approximately 5B-parameter \textit{Gemini-2.5-Flash}~\cite{comanici2025gemini} model, attains 45.5% accuracy. These results demonstrate that careful discretization and context selection can cut inference cost by over 2x while preserving the advantages of prompt-based AMC and enabling practical in-the-loop use.

