---
layout: default
title: HyMAD: A Hybrid Multi-Activity Detection Approach for Border Surveillance and Monitoring
---

# HyMAD: A Hybrid Multi-Activity Detection Approach for Border Surveillance and Monitoring

**arXiv**: [2511.14698v1](https://arxiv.org/abs/2511.14698) | [PDF](https://arxiv.org/pdf/2511.14698.pdf)

**作者**: Sriram Srinivasan, Srinivasan Aruchamy, Siva Ram Krisha Vadali

---

## 💡 一句话要点

**提出HyMAD混合多活动检测方法，以解决边境监控中地震信号重叠活动识别问题**

**关键词**: `地震传感` `多活动检测` `时空特征融合` `自注意力机制` `多标签分类` `边境监控`

## 📋 核心要点

1. 核心问题：地震信号复杂噪声下，同时发生的人类入侵、动物移动和车辆活动难以准确区分
2. 方法要点：融合SincNet频谱特征、RNN时序依赖、自注意力层和跨模态融合模块
3. 实验或效果：在真实边境数据集上验证，能泛化处理复杂同时活动场景，性能具竞争力

## 📄 摘要（原文）

> Seismic sensing has emerged as a promising solution for border surveillance and monitoring; the seismic sensors that are often buried underground are small and cannot be noticed easily, making them difficult for intruders to detect, avoid, or vandalize. This significantly enhances their effectiveness compared to highly visible cameras or fences. However, accurately detecting and distinguishing between overlapping activities that are happening simultaneously, such as human intrusions, animal movements, and vehicle rumbling, remains a major challenge due to the complex and noisy nature of seismic signals. Correctly identifying simultaneous activities is critical because failing to separate them can lead to misclassification, missed detections, and an incomplete understanding of the situation, thereby reducing the reliability of surveillance systems. To tackle this problem, we propose HyMAD (Hybrid Multi-Activity Detection), a deep neural architecture based on spatio-temporal feature fusion. The framework integrates spectral features extracted with SincNet and temporal dependencies modeled by a recurrent neural network (RNN). In addition, HyMAD employs self-attention layers to strengthen intra-modal representations and a cross-modal fusion module to achieve robust multi-label classification of seismic events. e evaluate our approach on a dataset constructed from real-world field recordings collected in the context of border surveillance and monitoring, demonstrating its ability to generalize to complex, simultaneous activity scenarios involving humans, animals, and vehicles. Our method achieves competitive performance and offers a modular framework for extending seismic-based activity recognition in real-world security applications.

