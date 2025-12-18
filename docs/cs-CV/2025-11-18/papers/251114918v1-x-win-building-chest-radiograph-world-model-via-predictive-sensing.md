---
layout: default
title: X-WIN: Building Chest Radiograph World Model via Predictive Sensing
---

# X-WIN: Building Chest Radiograph World Model via Predictive Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14918" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14918v1</a>
  <a href="https://arxiv.org/pdf/2511.14918.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14918v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14918v1', 'X-WIN: Building Chest Radiograph World Model via Predictive Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zefan Yang, Ge Wang, James Hendler, Mannudeep K. Kalra, Pingkun Yan

**分类**: cs.CV

**发布日期**: 2025-11-18

---

## 💡 一句话要点

**X-WIN：通过预测感知构建胸部X光片世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `胸部X光片` `世界模型` `预测感知` `对比学习` `医学影像`

## 📋 核心要点

1. CXR作为2D图像，缺乏3D信息，限制了其在表征学习和疾病诊断中的应用。
2. X-WIN通过学习预测CT的2D投影，构建CXR世界模型，从而提取3D体积知识。
3. 实验表明，X-WIN在下游任务中优于现有模型，并能通过2D投影重建3D CT。

## 📝 摘要（中文）

胸部X光片（CXR）是疾病诊断的重要医学影像技术。然而，作为2D投影图像，CXR受到结构叠加的限制，无法捕捉3D解剖结构，这使得表征学习和疾病诊断充满挑战。为了解决这个问题，我们提出了一种名为X-WIN的新型CXR世界模型，它通过学习预测潜在空间中的2D投影，从胸部CT中提取体积知识。核心思想是，具有内在3D解剖结构知识的世界模型可以预测3D空间中各种变换下的CXR。在投影预测过程中，我们引入了一种亲和力引导的对比对齐损失，该损失利用相互相似性来捕获来自同一体积的投影之间的丰富相关信息。为了提高模型的适应性，我们通过掩码图像建模将真实的CXR纳入训练，并采用领域分类器来鼓励真实CXR和模拟CXR具有统计上相似的表示。综合实验表明，X-WIN在使用线性探测和少样本微调的各种下游任务上优于现有的基础模型。X-WIN还展示了渲染2D投影以重建3D CT体积的能力。

## 🔬 方法详解

**问题定义**：胸部X光片（CXR）是2D投影图像，缺乏3D结构信息，导致难以进行有效的表征学习和疾病诊断。现有的方法难以充分利用CXR图像中的空间关系和解剖结构信息，限制了诊断的准确性和可靠性。

**核心思路**：X-WIN的核心思路是通过学习预测CXR图像，构建一个能够理解3D解剖结构的世界模型。该模型通过从胸部CT图像中提取3D体积知识，并学习将这些知识投影到2D CXR图像上，从而能够预测在不同视角和变换下的CXR图像。这种方法使得模型能够学习到CXR图像中隐含的3D结构信息，从而提高表征学习和疾病诊断的性能。

**技术框架**：X-WIN的整体框架包括以下几个主要模块：1) CT图像编码器：用于提取CT图像的3D特征表示。2) 投影预测器：用于将CT特征投影到2D CXR图像上。3) CXR图像编码器：用于提取真实CXR图像的特征表示。4) 亲和力引导的对比对齐损失：用于对齐预测的CXR图像和真实的CXR图像的特征表示。5) 掩码图像建模：用于提高模型对真实CXR图像的适应性。6) 领域分类器：用于鼓励真实CXR图像和模拟CXR图像具有统计上相似的表示。

**关键创新**：X-WIN的关键创新在于构建了一个CXR世界模型，该模型能够理解3D解剖结构并预测CXR图像。此外，该模型还引入了一种亲和力引导的对比对齐损失，该损失能够有效地对齐预测的CXR图像和真实的CXR图像的特征表示。与现有方法相比，X-WIN能够更好地利用CXR图像中的3D结构信息，从而提高表征学习和疾病诊断的性能。

**关键设计**：在亲和力引导的对比对齐损失中，使用了互相似度来捕获来自同一体积的投影之间的丰富相关信息。掩码图像建模通过随机mask CXR图像的部分区域，并要求模型预测被mask的区域，从而提高模型对CXR图像的理解能力。领域分类器用于区分真实CXR图像和模拟CXR图像，并鼓励模型学习到与领域无关的特征表示。

## 📊 实验亮点

实验结果表明，X-WIN在多种下游任务上优于现有的基础模型，包括线性探测和少样本微调。X-WIN还展示了通过渲染2D投影重建3D CT体积的能力，验证了其对3D解剖结构的理解。具体的性能数据和对比基线在论文中有详细描述。

## 🎯 应用场景

X-WIN可应用于多种医学影像分析任务，例如疾病诊断、病灶定位、图像配准和图像重建。通过构建CXR世界模型，可以提高诊断的准确性和效率，减少对医生经验的依赖。该研究的成果有助于推动医学影像智能化发展，为临床应用提供更强大的工具。

## 📄 摘要（原文）

> Chest X-ray radiography (CXR) is an essential medical imaging technique for disease diagnosis. However, as 2D projectional images, CXRs are limited by structural superposition and hence fail to capture 3D anatomies. This limitation makes representation learning and disease diagnosis challenging. To address this challenge, we propose a novel CXR world model named X-WIN, which distills volumetric knowledge from chest computed tomography (CT) by learning to predict its 2D projections in latent space. The core idea is that a world model with internalized knowledge of 3D anatomical structure can predict CXRs under various transformations in 3D space. During projection prediction, we introduce an affinity-guided contrastive alignment loss that leverages mutual similarities to capture rich, correlated information across projections from the same volume. To improve model adaptability, we incorporate real CXRs into training through masked image modeling and employ a domain classifier to encourage statistically similar representations for real and simulated CXRs. Comprehensive experiments show that X-WIN outperforms existing foundation models on diverse downstream tasks using linear probing and few-shot fine-tuning. X-WIN also demonstrates the ability to render 2D projections for reconstructing a 3D CT volume.

