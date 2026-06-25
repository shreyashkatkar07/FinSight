import { useMutation, useQueryClient } from "@tanstack/react-query";

import { ingestText } from "../api";

export function useAddTransaction() {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: ingestText,

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["dashboard"],
      });
    },
  });

  return mutation;
}