---
layout: default
title: ConnectomeBench: Can LLMs Proofread the Connectome?
---

# ConnectomeBench: Can LLMs Proofread the Connectome?

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.05542" target="_blank" class="toolbar-btn">arXiv: 2511.05542v1</a>
    <a href="https://arxiv.org/pdf/2511.05542.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05542v1" 
            onclick="toggleFavorite(this, '2511.05542v1', 'ConnectomeBench: Can LLMs Proofread the Connectome?')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jeff Brown, Andrew Kirjner, Annika Vivekananthan, Ed Boyden

**分类**: q-bio.NC, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-31

**备注**: To appear in NeurIPS 2025 Datasets and Benchmarks Track

**🔗 代码/项目**: [GITHUB](https://github.com/jffbrwn2/ConnectomeBench) | [HUGGINGFACE](https://huggingface.co/datasets/jeffbbrown2)

---

## 💡 一句话要点

**ConnectomeBench：评估LLM在神经连接体校对中的能力，探索AI辅助神经科学**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经连接体` `大型语言模型` `多模态学习` `图像分割` `错误校正` `基准测试` `人工智能` `神经科学`

## 📋 核心要点

1. 神经连接体构建面临人工校对耗时巨大的挑战，亟需自动化解决方案。
2. ConnectomeBench基准测试旨在评估LLM在神经连接体校对任务中的潜力。
3. 实验结果表明，LLM在片段识别和分割错误校正方面表现出潜力，但在合并错误识别方面仍有不足。

## 📝 摘要（中文）

神经连接体（Connectome）的构建，即绘制生物大脑中的神经连接图谱，目前需要大量的人工校对图像和机器学习辅助分割的数据。随着利用AI智能体自动执行重要科学任务的呼声日益高涨，本文探讨了当前AI系统是否能够执行数据校对所需的多个任务。我们提出了ConnectomeBench，这是一个多模态基准，用于评估大型语言模型（LLM）在三个关键校对任务中的能力：片段类型识别、分割错误校正和合并错误检测。我们使用来自两个大型开源数据集（小鼠视觉皮层的立方毫米和完整的果蝇大脑）的专家标注数据，评估了包括Claude 3.7/4 Sonnet、o4-mini、GPT-4.1、GPT-4o等专有模型以及InternVL-3和NVLM等开源模型。结果表明，当前模型在片段识别（52-82%的平衡准确率，而随机概率为20-25%）和二元/多项选择分割错误校正（75-85%的准确率，而随机概率为50%）方面表现出惊人的高性能，但在合并错误识别任务中表现不佳。总的来说，虽然最好的模型仍然落后于专家水平，但它们展示了有希望的能力，最终可能使它们能够增强甚至取代神经连接体中的人工校对。

## 🔬 方法详解

**问题定义**：神经连接体构建依赖于图像分割和人工校对，人工校对耗时且容易出错。现有方法难以有效识别和纠正分割错误（包括分割过细和合并错误），阻碍了神经连接体研究的进展。

**核心思路**：利用大型语言模型（LLM）的多模态理解能力，将神经连接体数据（包括图像和文本描述）作为输入，让LLM学习识别和纠正分割错误。这种方法的核心在于利用LLM的知识和推理能力来辅助人工校对。

**技术框架**：ConnectomeBench包含三个主要任务：片段类型识别、分割错误校正和合并错误检测。每个任务都包含图像数据和文本描述。LLM接收这些数据作为输入，并输出相应的预测结果。评估指标包括平衡准确率和准确率。整体流程包括数据准备、模型推理和结果评估。

**关键创新**：该研究的关键创新在于将LLM应用于神经连接体校对任务，并提出了ConnectomeBench基准测试。这是首次系统性地评估LLM在神经连接体校对中的能力。与传统方法相比，LLM能够利用其强大的语言理解和推理能力来辅助校对，有望提高校对效率和准确性。

**关键设计**：ConnectomeBench使用了来自两个大型开源数据集的数据：小鼠视觉皮层和果蝇大脑。评估了多种LLM，包括专有模型（如Claude 3.7/4 Sonnet、GPT-4.1、GPT-4o）和开源模型（如InternVL-3、NVLM）。针对不同的任务，采用了不同的评估指标。例如，片段类型识别使用平衡准确率，分割错误校正使用准确率。

## 📊 实验亮点

实验结果表明，LLM在片段识别任务中取得了52-82%的平衡准确率，远高于随机概率（20-25%）。在二元/多项选择分割错误校正任务中，LLM取得了75-85%的准确率，也高于随机概率（50%）。这些结果表明，LLM在神经连接体校对方面具有潜力，但仍需进一步改进，尤其是在合并错误识别方面。

## 🎯 应用场景

该研究成果可应用于神经科学领域，加速神经连接体的构建和分析。通过利用LLM辅助人工校对，可以显著提高校对效率，降低人工成本，并减少人为错误。未来，该技术有望应用于其他生物图像分析领域，例如细胞分割和组织结构分析，促进生物医学研究的进展。

## 📄 摘要（原文）

> Connectomics - the mapping of neural connections in an organism's brain - currently requires extraordinary human effort to proofread the data collected from imaging and machine-learning assisted segmentation. With the growing excitement around using AI agents to automate important scientific tasks, we explore whether current AI systems can perform multiple tasks necessary for data proofreading. We introduce ConnectomeBench, a multimodal benchmark evaluating large language model (LLM) capabilities in three critical proofreading tasks: segment type identification, split error correction, and merge error detection. Using expert annotated data from two large open-source datasets - a cubic millimeter of mouse visual cortex and the complete Drosophila brain - we evaluate proprietary multimodal LLMs including Claude 3.7/4 Sonnet, o4-mini, GPT-4.1, GPT-4o, as well as open source models like InternVL-3 and NVLM. Our results demonstrate that current models achieve surprisingly high performance in segment identification (52-82% balanced accuracy vs. 20-25% chance) and binary/multiple choice split error correction (75-85% accuracy vs. 50% chance) while generally struggling on merge error identification tasks. Overall, while the best models still lag behind expert performance, they demonstrate promising capabilities that could eventually enable them to augment and potentially replace human proofreading in connectomics. Project page: https://github.com/jffbrwn2/ConnectomeBench and Dataset https://huggingface.co/datasets/jeffbbrown2/ConnectomeBench/tree/main

