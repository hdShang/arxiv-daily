---
layout: default
title: GRAID: Enhancing Spatial Reasoning of VLMs Through High-Fidelity Data Generation
---

# GRAID: Enhancing Spatial Reasoning of VLMs Through High-Fidelity Data Generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22118" target="_blank" class="toolbar-btn">arXiv: 2510.22118v2</a>
    <a href="https://arxiv.org/pdf/2510.22118.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22118v2" 
            onclick="toggleFavorite(this, '2510.22118v2', 'GRAID: Enhancing Spatial Reasoning of VLMs Through High-Fidelity Data Generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Karim Elmaaroufi, Liheng Lai, Justin Svegliato, Yutong Bai, Sanjit A. Seshia, Matei Zaharia

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-25 (更新: 2025-10-28)

**备注**: 22 pages, 3 figures, 3 tables, project page: https://ke7.github.io/graid/

---

## 💡 一句话要点

**GRAID：通过高质量数据生成增强视觉语言模型空间推理能力**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `视觉语言模型` `空间推理` `数据生成` `2D几何推理` `目标检测`

## 📋 核心要点

1. 现有视觉语言模型在空间推理方面存在不足，限制了其在许多实际应用中的表现。
2. GRAID利用2D几何图元推断空间关系，避免了3D重建误差和生成幻觉，从而生成高质量的训练数据。
3. 实验表明，使用GRAID生成的数据训练的模型，在空间推理任务上取得了显著的性能提升，并具有良好的泛化能力。

## 📝 摘要（中文）

视觉语言模型(VLMs)在许多视觉语言任务上表现出色，但常常在空间推理方面遇到困难，而空间推理是许多应用的前提。实证研究表明，当前训练数据生成流程产生的数据集的人工验证率仅为57.6%。这些低验证率源于现有局限性：单图像3D重建引入了级联建模误差，需要较大的答案容差；而基于字幕的方法需要超详细的标注，并容易出现生成幻觉。我们提出了GRAID，其核心思想是定性的空间关系可以仅从2D几何图元可靠地确定。通过仅操作来自标准目标检测器的2D边界框，GRAID避免了3D重建误差和生成幻觉，从而生成比现有工具更高质量的数据集，这已通过人工评估验证。我们将我们的框架应用于BDD100k、NuImages和Waymo数据集，生成超过850万个高质量VQA对，创建的问题涵盖空间关系、计数、排名和大小比较。我们评估了其中一个数据集，发现它实现了91.16%的人工验证准确率，而最近一项工作生成的数据集仅为57.6%。至关重要的是，我们证明了当在GRAID数据上训练时，模型学习到的空间推理概念可以泛化：在6种问题类型上微调的模型在超过10种保留类型上有所改进，Llama 3.2B 11B在BDD上准确率提高了47.5%，在NuImages上提高了37.9%，并且在所有问题类型上训练时，在BLINK等多个现有基准上取得了改进。GRAID框架、数据集和其他信息可以在此处找到。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在空间推理能力上存在不足，主要原因是训练数据质量不高。现有的数据生成方法，如基于单图像3D重建的方法，会引入级联建模误差，而基于caption的方法需要精细的标注，且容易产生幻觉，导致生成的数据质量较低，限制了模型的学习效果。

**核心思路**：GRAID的核心思路是利用2D几何图元（例如，目标检测的边界框）来可靠地推断空间关系。这种方法避免了复杂的3D重建过程，从而消除了由此产生的误差。同时，由于直接基于检测结果进行推理，避免了生成式模型可能产生的幻觉，保证了数据质量。

**技术框架**：GRAID框架主要包括以下几个阶段：1) 使用标准的目标检测器获取图像中物体的2D边界框；2) 基于这些边界框，定义各种空间关系（例如，左边、右边、上方、下方、包含等）；3) 根据这些空间关系，自动生成视觉问答（VQA）对，包括问题和对应的答案；4) 对生成的数据进行人工验证，确保数据质量。该框架可以应用于各种包含目标检测标注的数据集。

**关键创新**：GRAID最重要的创新在于其数据生成方法，它完全依赖于2D几何信息，避免了3D重建和生成式模型，从而保证了生成数据的质量和可靠性。与现有方法相比，GRAID能够生成更高质量、更准确的VQA数据集，从而显著提升视觉语言模型的空间推理能力。

**关键设计**：GRAID的关键设计包括：1) 精心设计的空间关系集合，涵盖了常见的空间推理场景；2) 自动化的VQA对生成流程，能够高效地生成大规模数据集；3) 人工验证环节，用于过滤掉错误或不准确的数据，进一步提升数据质量。论文中没有明确提及具体的参数设置或损失函数，因为其重点在于数据生成方法本身，而非模型训练的细节。

## 📊 实验亮点

GRAID生成的数据集在人工验证中达到了91.16%的准确率，显著高于现有方法的57.6%。使用GRAID数据训练的Llama 3.2B 11B模型在BDD和NuImages数据集上分别取得了47.5%和37.9%的准确率提升。此外，该模型在BLINK等现有基准上也取得了改进，表明GRAID能够有效提升视觉语言模型的空间推理能力和泛化能力。

## 🎯 应用场景

GRAID的研究成果可广泛应用于自动驾驶、机器人导航、智能监控等领域。高质量的空间推理能力对于这些应用至关重要，例如，自动驾驶系统需要准确理解车辆周围环境的空间关系，才能做出正确的决策。GRAID提供了一种有效的方法来提升视觉语言模型的空间推理能力，从而推动这些领域的发展。

## 📄 摘要（原文）

> Vision Language Models (VLMs) achieve strong performance on many vision-language tasks but often struggle with spatial reasoning$\unicode{x2014}$a prerequisite for many applications. Empirically, we find that a dataset produced by a current training data generation pipeline has a 57.6% human validation rate. These rates stem from current limitations: single-image 3D reconstruction introduces cascading modeling errors and requires wide answer tolerances, while caption-based methods require hyper-detailed annotations and suffer from generative hallucinations. We present GRAID, built on the key insight that qualitative spatial relationships can be reliably determined from 2D geometric primitives alone. By operating exclusively on 2D bounding boxes from standard object detectors, GRAID avoids both 3D reconstruction errors and generative hallucinations, resulting in datasets that are of higher quality than existing tools that produce similar datasets as validated by human evaluations. We apply our framework to the BDD100k, NuImages, and Waymo datasets, generating over 8.5 million high-quality VQA pairs creating questions spanning spatial relations, counting, ranking, and size comparisons. We evaluate one of the datasets and find it achieves 91.16% human-validated accuracy$\unicode{x2014}$compared to 57.6% on a dataset generated by recent work. Critically, we demonstrate that when trained on GRAID data, models learn spatial reasoning concepts that generalize: models fine-tuned on 6 question types improve on over 10 held-out types, with accuracy gains of 47.5% on BDD and 37.9% on NuImages for Llama 3.2B 11B, and when trained on all questions types, achieve improvements on several existing benchmarks such as BLINK. The GRAID framework, datasets, and additional information can be found $\href{this https URL}{here}$.

