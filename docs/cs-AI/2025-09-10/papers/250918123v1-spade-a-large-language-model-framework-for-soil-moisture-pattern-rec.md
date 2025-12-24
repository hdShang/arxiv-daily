---
layout: default
title: "SPADE: A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture"
---

# SPADE: A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18123" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18123v1</a>
  <a href="https://arxiv.org/pdf/2509.18123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18123v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18123v1', 'SPADE: A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yeonju Lee, Rui Qi Chen, Joseph Oboamah, Po Nien Su, Wei-zhen Liang, Yeyin Shi, Lu Gan, Yongsheng Chen, Xin Qiao, Jing Li

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**SPADE：利用大语言模型进行精准农业中的土壤湿度模式识别与异常检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `土壤湿度监测` `精准农业` `大语言模型` `异常检测` `时间序列分析`

## 📋 核心要点

1. 现有土壤湿度时间序列分析方法依赖于基于阈值的规则或数据密集型机器学习模型，缺乏适应性和可解释性。
2. SPADE框架将时间序列数据转换为文本，利用大语言模型ChatGPT-4.1进行零样本分析，识别灌溉模式和异常。
3. 实验表明，SPADE在异常检测和灌溉事件检测方面优于现有方法，并能生成可解释的报告。

## 📝 摘要（中文）

本研究提出了一种名为SPADE（土壤湿度模式与异常检测）的集成框架，该框架利用大型语言模型（LLM）联合检测土壤湿度时间序列数据中的灌溉模式和异常。SPADE利用ChatGPT-4.1的先进推理和指令遵循能力，实现零样本分析，无需特定任务的标注或微调。通过将时间序列数据转换为文本表示并设计领域相关的提示模板，SPADE能够识别灌溉事件，估计净灌溉增益，检测和分类异常，并生成结构化的、可解释的报告。在美国商业和实验农场种植多种作物的真实土壤湿度传感器数据上进行了实验。结果表明，SPADE在异常检测方面优于现有方法，实现了更高的召回率和F1分数，并准确地分类了异常类型。此外，SPADE在检测灌溉事件方面实现了高精度和召回率，表明其具有准确捕获灌溉模式的强大能力。SPADE的报告提供了土壤湿度分析的可解释性和可用性。这项研究突出了LLM作为可扩展、适应性强的精准农业工具的潜力，它能够整合定性知识和数据驱动的推理，从而为准确的土壤湿度监测和改进的灌溉调度提供可操作的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决精准农业中土壤湿度模式识别和异常检测的问题。现有方法，如基于阈值的规则或数据驱动的机器学习模型，存在适应性差、可解释性弱以及需要大量标注数据等痛点。这些限制阻碍了对土壤湿度数据的有效分析和利用，进而影响灌溉决策。

**核心思路**：论文的核心思路是将土壤湿度时间序列数据转化为文本描述，然后利用大型语言模型（LLM）的强大推理能力，通过设计合适的提示（Prompt）来指导LLM识别灌溉模式、检测异常并生成可解释的报告。这种方法旨在利用LLM的零样本学习能力，减少对标注数据的依赖，并提高模型的可解释性和泛化能力。

**技术框架**：SPADE框架主要包含以下几个阶段：1) 数据预处理：对原始土壤湿度时间序列数据进行清洗和格式化。2) 文本转换：将时间序列数据转换为文本描述，例如描述土壤湿度随时间的变化趋势。3) 提示工程：设计领域相关的提示模板，指导LLM执行特定的任务，如识别灌溉事件、检测异常等。4) LLM推理：使用ChatGPT-4.1等LLM对文本描述进行分析，并根据提示生成结构化的报告。5) 结果评估：对LLM的输出结果进行评估，验证其准确性和可靠性。

**关键创新**：该论文最重要的技术创新点在于将大型语言模型应用于土壤湿度模式识别和异常检测任务，并提出了一种基于文本转换和提示工程的零样本学习方法。与传统的机器学习方法相比，SPADE无需大量的标注数据，并且具有更强的可解释性和泛化能力。此外，SPADE能够整合定性知识和数据驱动的推理，从而为灌溉决策提供更全面的信息。

**关键设计**：关键设计包括：1) 文本转换策略：如何将时间序列数据有效地转换为文本描述，以便LLM能够理解和处理。2) 提示模板设计：如何设计合适的提示模板，指导LLM执行特定的任务，例如，使用自然语言描述灌溉事件的特征，并要求LLM识别符合这些特征的时间段。3) 异常分类体系：如何定义和分类不同类型的土壤湿度异常，以便LLM能够准确地识别和报告这些异常。

## 📊 实验亮点

SPADE在真实土壤湿度数据集上进行了实验，结果表明，在异常检测方面，SPADE的召回率和F1分数均优于现有方法，并且能够准确地分类异常类型。此外，SPADE在检测灌溉事件方面也实现了高精度和召回率，证明了其强大的模式识别能力。

## 🎯 应用场景

SPADE框架可应用于精准农业领域，帮助农民和农业专家更好地理解土壤湿度模式，及时发现异常情况，从而优化灌溉策略，提高作物产量和资源利用效率。该研究的成果有助于推动农业智能化发展，实现可持续农业生产。

## 📄 摘要（原文）

> Accurate interpretation of soil moisture patterns is critical for irrigation scheduling and crop management, yet existing approaches for soil moisture time-series analysis either rely on threshold-based rules or data-hungry machine learning or deep learning models that are limited in adaptability and interpretability. In this study, we introduce SPADE (Soil moisture Pattern and Anomaly DEtection), an integrated framework that leverages large language models (LLMs) to jointly detect irrigation patterns and anomalies in soil moisture time-series data. SPADE utilizes ChatGPT-4.1 for its advanced reasoning and instruction-following capabilities, enabling zero-shot analysis without requiring task-specific annotation or fine-tuning. By converting time-series data into a textual representation and designing domain-informed prompt templates, SPADE identifies irrigation events, estimates net irrigation gains, detects, classifies anomalies, and produces structured, interpretable reports. Experiments were conducted on real-world soil moisture sensor data from commercial and experimental farms cultivating multiple crops across the United States. Results demonstrate that SPADE outperforms the existing method in anomaly detection, achieving higher recall and F1 scores and accurately classifying anomaly types. Furthermore, SPADE achieved high precision and recall in detecting irrigation events, indicating its strong capability to capture irrigation patterns accurately. SPADE's reports provide interpretability and usability of soil moisture analytics. This study highlights the potential of LLMs as scalable, adaptable tools for precision agriculture, which is capable of integrating qualitative knowledge and data-driven reasoning to produce actionable insights for accurate soil moisture monitoring and improved irrigation scheduling from soil moisture time-series data.

