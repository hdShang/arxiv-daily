---
layout: default
title: BlendCLIP: Bridging Synthetic and Real Domains for Zero-Shot 3D Object Classification with Multimodal Pretraining
---

# BlendCLIP: Bridging Synthetic and Real Domains for Zero-Shot 3D Object Classification with Multimodal Pretraining

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.18244" target="_blank" class="toolbar-btn">arXiv: 2510.18244v1</a>
    <a href="https://arxiv.org/pdf/2510.18244.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18244v1" 
            onclick="toggleFavorite(this, '2510.18244v1', 'BlendCLIP: Bridging Synthetic and Real Domains for Zero-Shot 3D Object Classification with Multimodal Pretraining')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ajinkya Khoche, Gergő László Nagy, Maciej Wozniak, Thomas Gustafsson, Patric Jensfelt

**分类**: cs.CV

**发布日期**: 2025-10-21

**备注**: Under Review

**🔗 代码/项目**: [GITHUB](https://github.com/kesu1/BlendCLIP)

---

## 💡 一句话要点

**BlendCLIP：通过多模态预训练桥接合成与真实域，实现零样本3D物体分类**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本学习` `3D物体分类` `多模态学习` `领域自适应` `课程学习` `CLIP` `自动驾驶`

## 📋 核心要点

1. 现有零样本3D物体分类方法难以应对合成数据与真实LiDAR数据间的领域差异，导致泛化能力不足。
2. BlendCLIP通过多模态预训练，结合合成数据的语义信息和真实数据的特征，弥合领域鸿沟。
3. 实验表明，仅需少量真实数据即可显著提升零样本分类精度，并在nuScenes数据集上取得SOTA结果。

## 📝 摘要（中文）

零样本3D物体分类对于自动驾驶等实际应用至关重要，但常受到训练所用的合成数据与真实世界中稀疏、嘈杂的激光雷达扫描之间显著的领域差距的阻碍。当前仅在合成数据上训练的方法无法泛化到室外场景，而仅在真实数据上训练的方法缺乏识别稀有或未见物体的语义多样性。我们引入BlendCLIP，一个多模态预训练框架，通过策略性地结合两个领域的优势来弥合这种合成到真实的差距。我们首先提出了一个pipeline，用于生成大规模的物体级别三元组数据集，包含点云、图像和文本描述，直接从真实世界驾驶数据和人工标注的3D框中挖掘。我们的核心贡献是一种基于课程的数据混合策略，该策略首先将模型置于语义丰富的合成CAD数据中，然后再逐步将其适应真实世界扫描的特定特征。实验表明，我们的方法具有很高的标签效率：在训练中每批次引入低至1.5％的真实世界样本，即可将nuScenes基准上的零样本精度提高27％。因此，我们的最终模型在具有挑战性的室外数据集（如nuScenes和TruckScenes）上实现了最先进的性能，在nuScenes上比最佳现有方法提高了19.3％，同时在各种合成基准上保持了强大的泛化能力。我们的发现表明，有效的领域自适应，而不是全面的真实世界标注，是解锁鲁棒的开放词汇3D感知的关键。我们的代码和数据集将在接受后发布在https://github.com/kesu1/BlendCLIP。

## 🔬 方法详解

**问题定义**：论文旨在解决零样本3D物体分类中，模型在合成数据上训练后，难以泛化到真实世界LiDAR数据的问题。现有方法要么依赖大量真实数据标注，成本高昂；要么仅使用合成数据，领域差异导致性能下降。

**核心思路**：论文的核心思路是利用多模态预训练，结合合成数据的语义信息和真实数据的特征，通过课程学习的方式，逐步将模型从合成域迁移到真实域。这样既能利用合成数据的丰富语义信息，又能适应真实数据的特点，提高模型的泛化能力。

**技术框架**：BlendCLIP框架包含以下几个主要阶段：1) 构建大规模多模态数据集，包含合成CAD模型和真实世界驾驶数据（点云、图像、文本描述）；2) 使用课程学习策略，先在合成数据上进行预训练，使模型学习通用的3D物体表示；3) 逐步引入真实数据，通过数据混合的方式，使模型适应真实数据的特征；4) 在目标数据集上进行零样本评估。

**关键创新**：论文的关键创新在于提出了基于课程的数据混合策略，该策略能够有效地将模型从合成域迁移到真实域。与直接在混合数据集上训练相比，课程学习能够更好地利用合成数据的语义信息，并逐步适应真实数据的特征，从而提高模型的泛化能力。

**关键设计**：论文的关键设计包括：1) 数据集构建：从真实世界驾驶数据中挖掘物体级别的三元组数据（点云、图像、文本描述）；2) 课程学习策略：设计合适的课程，控制合成数据和真实数据的混合比例，逐步增加真实数据的比例；3) 多模态融合：使用CLIP模型作为骨干网络，将点云、图像和文本信息融合在一起，学习统一的物体表示。

## 📊 实验亮点

BlendCLIP在nuScenes数据集上实现了SOTA的零样本3D物体分类性能，相比现有最佳方法提升了19.3%。通过引入少量（1.5%）真实数据，即可将零样本精度提升27%。实验结果表明，有效的领域自适应是提升零样本3D感知能力的关键，而无需依赖大规模的真实数据标注。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能安防等领域。通过提升零样本3D物体分类的性能，可以使机器人在未知环境中更好地感知和理解周围环境，从而实现更安全、更智能的自主行为。该方法降低了对大量标注数据的依赖，具有重要的实际应用价值。

## 📄 摘要（原文）

> Zero-shot 3D object classification is crucial for real-world applications like autonomous driving, however it is often hindered by a significant domain gap between the synthetic data used for training and the sparse, noisy LiDAR scans encountered in the real-world. Current methods trained solely on synthetic data fail to generalize to outdoor scenes, while those trained only on real data lack the semantic diversity to recognize rare or unseen objects.
>   We introduce BlendCLIP, a multimodal pretraining framework that bridges this synthetic-to-real gap by strategically combining the strengths of both domains. We first propose a pipeline to generate a large-scale dataset of object-level triplets -- consisting of a point cloud, image, and text description -- mined directly from real-world driving data and human annotated 3D boxes. Our core contribution is a curriculum-based data mixing strategy that first grounds the model in the semantically rich synthetic CAD data before progressively adapting it to the specific characteristics of real-world scans.
>   Our experiments show that our approach is highly label-efficient: introducing as few as 1.5\% real-world samples per batch into training boosts zero-shot accuracy on the nuScenes benchmark by 27\%. Consequently, our final model achieves state-of-the-art performance on challenging outdoor datasets like nuScenes and TruckScenes, improving over the best prior method by 19.3\% on nuScenes, while maintaining strong generalization on diverse synthetic benchmarks. Our findings demonstrate that effective domain adaptation, not full-scale real-world annotation, is the key to unlocking robust open-vocabulary 3D perception. Our code and dataset will be released upon acceptance on https://github.com/kesu1/BlendCLIP.

